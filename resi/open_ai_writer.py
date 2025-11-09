from openai import OpenAI
import json
import torch
import torch.nn.functional as F
import re

client = OpenAI()
open_ai_model = "gpt-4.1-nano"
embeddings_generator_model = "text-embedding-3-small"

def cover_letter_generator(
        job_desc: str,
        history,
        additional_prompts
    ):

    # if job desc is empty, then raise an error
    if job_desc == None or job_desc.strip() == '':
        raise ValueError('Job description cannot be empty')

    response = client.chat.completions.create(
        model=open_ai_model,
        messages=[
            {"role": "system", "content": "You are a top cover letter assistant that helps users tailor a cover letter for the job description"},
            {"role": "user", "content": f"""
            Given the job description below, generate a cover letter that is tailored as best as you can
            to the job description.
            
            Additional Requirements:
            Do not add any experience that is not in my history.
            If there is a skill in the job description that I do not posses, do not include it or talk about it.
            Do not include the closing part like Sincerely, [your name] or any "insert your content here"
            Do not use any em dashes.
             
            Job Description:
            {job_desc} 

            User work history:
            {history}

            Also take in any additional instructions from the user if any:
            {additional_prompts.strip()}

            Return only the paragraphs of the cover letter.
            """}
        ]
    )

    return response.choices[0].message.content

def generate_profile(
    job_desc: str,
    history: dict
) -> str:
    """
    Generate a resume profile from the user work history that best fits the job description
    """
    # Check if parameters are empty
    if job_desc == None or job_desc.strip() == '':
        raise ValueError('Job description cannot be empty')
    
    if history == None:
        raise ValueError('Job History cannot be empty')
    
    response = client.chat.completions.create(
        model=open_ai_model,
        messages=[
            {"role": "system", "content": "You are a top resume assistant that will help me tailor my resume as best as you can to the given job description."},
            {"role": "user", "content": f"""
            Based on the work history of provided below, please generate a short profile summary highlighting the best skills for the job description provided.
            Make the profile short and to the point.
            Do not include any experience that is not in provided.
            Do not use any em-dashes.
             
            Job Description:
            {job_desc}

            User work history:
            {history}
             
            """}
        ]
    )

    return response.choices[0].message.content

def generate_job_bullets(
        job_desc: str,
        history: dict,
        additional_prompts: str
    ) -> dict:

    # if job desc is empty, then raise an error
    if job_desc == None or job_desc.strip() == '':
        raise ValueError('Job description cannot be empty')

    response = client.chat.completions.create(
        model=open_ai_model,
        messages=[
            {"role": "system", "content": "You are a top resume assistant that will help me tailor my resume as best as you can to the given job description."},
            {"role": "user", "content": f"""
            
            Additional Requirements:
            Do not include any text outside the JSON.
            Do not add any experience that is not already in the resume history.
            When rewriting the bullet points, only specify skills that are relevant to the industry in my history.
            For example:  Built and maintained end-to-end data pipelines using Python microservices to support data-driven insights for [industry in my history here]
            Only do this if absolutely necessary to better fit the bullet to the job.
            Do not use em-dashes in the rewritten bullets.
             
            Job Description:
            {job_desc}

            User work history:
            {history}

            Return a JSON array where each element is an object with the following fields:
            - "role": job title
            - "company": company name
            - "dates": employment dates (if provided)
            - "experience": a list of 5 bullet points tailored to the job description

            The response should look like this:
            [
            {{
                "role": "Job Title",
                "company": "Company Name",
                "dates": "Year-Year",
                "experience": [
                "Tailored bullet point 1",
                ...
                ]
            }},
            ... continue with the rest of the jobs using the same format
            ]

            Also take in any additional instructions from the user if any:
            {additional_prompts.strip()}
            """}
        ]
    )
    
    return json.loads(response.choices[0].message.content)

def compute_similarity(
        job_desc: str,
        resume_data: dict,
        round_to: int = 3
    ):

    # Normalize and tokenize
    job_sentences = re.split(r'(?<=[.!?])\s+', job_desc.strip())
    job_sentences = [s for s in job_sentences if len(s) > 10]
    
    resume_texts = []
    for key, val in resume_data.items():
        if isinstance(val, list):
            resume_texts.extend(val)
        else:
            resume_texts.append(val)
    
    # Embed all in batch
    all_inputs = job_sentences + resume_texts
    embeddings = client.embeddings.create(model=embeddings_generator_model, input=all_inputs).data
    tensors = [torch.tensor(x.embedding) for x in embeddings]
    
    job_embeds = tensors[:len(job_sentences)]
    resume_embeds = tensors[len(job_sentences):]
    
    # Normalize
    job_matrix = F.normalize(torch.stack(job_embeds), dim=1)
    resume_matrix = F.normalize(torch.stack(resume_embeds), dim=1)
    
    # Full cosine similarity matrix
    sim_matrix = torch.mm(job_matrix, resume_matrix.T)
    
    # Compute mean of top N matches per job sentence
    top_n = 3
    top_scores, _ = torch.topk(sim_matrix, top_n, dim=1)
    avg_top = torch.mean(top_scores, dim=1)
    
    # Aggregate
    overall_score = torch.mean(avg_top).item()
    
    return {
        "overall_score": round(overall_score, round_to),
        "details": [
            {"job_sentence": job_sentences[i], "avg_top_n": round(avg_top[i].item(), round_to)}
            for i in range(len(job_sentences))
        ]
    }
