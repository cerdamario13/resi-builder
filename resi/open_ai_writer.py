from openai import OpenAI
import json

client = OpenAI()
open_ai_model = "gpt-4.1-nano"

def cover_letter_generator(metadata: dict, history):

    # if job desc is empty, then raise an error
    if metadata['job_desc'].strip() == '':
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
            {metadata['job_desc']} 

            User work history:
            {history}

            Also take in any additional instructions from the user if any:
            {metadata.get('additional_message', '')}

            Return only the paragraphs of the cover letter.
            """}
        ]
    )

    return response.choices[0].message.content

def generate_job_bullets(metadata: dict, history: dict) -> dict:

    # if job desc is empty, then raise an error
    if metadata['job_desc'].strip() == '':
        raise ValueError('Job description cannot be empty')

    response = client.chat.completions.create(
        model=open_ai_model,
        messages=[
            {"role": "system", "content": "You are a top resume assistant that will help me tailor my resume as best as you can to the given job description."},
            {"role": "user", "content": f"""
            
            Additional Requirements:
            Do not include any text outside the JSON.
            Do not add any experience that is not already in the resume history.
            When rewriting the bullet points, only specify skills are relevant to the industry in my history.
            For example:  Built and maintained end-to-end data pipelines using Python microservices to support data-driven insights for [industry in my history here]
            Only do this if absolutely necessary to better fit the bullet to the job.
            Do not use em-dashes in the rewritten bullets.
             
            Job Description:
            {metadata['job_desc']}

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
            {metadata.get('additional_message', '')}
            """}
        ]
    )
    
    return json.loads(response.choices[0].message.content)