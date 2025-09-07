# Resi-builder

Create a resume and cover letter tailored to a specific job description using AI.

## Installation

```
pip install resi-builder
```

## Requirements

```python
reportlab
openai
```

An opeanAI API key is also required when generating the preview resume/cover letter. This can be stored as an environment variable.

## Personal Information
resi-builder does not pass personal information to the LLM aside from Name. For more information see `build_resume_preview` function in `resume` directory.

## Build User History

The following can be a JSON file or a python dictionary

```
{
  "contact_info": {
    "name": "",
    "phone": "",
    "email": "",
    "linkedIn": ""
  },
  "education": [
    {
      "school": "",
      "degree": "",
      "field_of_study": "",
      "location": ""
    }
  ],
  "history": [
    {
      "role": "",
      "company": "",
      "dates": "",
      "experience": [],
      "industry": []
    }
  ],
  "activities_and_interests": "",
  "profile": "",
  "skills": []
}
```

## Build Resume

In order to make a preview resume use the following


```python
import resi

# import the job desc from a text file
with open('job_desc.txt', 'r') as f:
    job_desc = f.read()

# Job metadata
metadata = {
    'job_desc': job_desc,
    'additional_message': '', # Optional
}

# Build the preview data - output will be a python dictionary
resume_data =  resi.resume.build_resume_preview(
    metadata,
    'user_history.json', # Importing a file via file path
)

# resume_metadata
resume_metadata = {
    'resume_file_name': 'resume.pdf', # Optional
    'resume_data': resume_data
}

# Build the file
resi.resume.build_resume_pdf(
    resume_metadata,
    'user_history.json' # can be a file path or a dict
)


```

## Build Cover Letter

```python
import resi

# import the job desc from a text file
with open('job_desc.txt', 'r') as f:
    job_desc = f.read()

# Job metadata
metadata = {
    'job_desc': job_desc,
    'additional_message': '', # Optional
}

# Build the preview data - output will be a python dictionary
cover_letter_data =  resi.cover_letter.build_cover_letter_preview(
    metadata,
    'user_history.json', # Importing a file via file path
)

# cover letter metadata
cover_letter_metadata = {
    'hiring_manager': 'Mr. Weyland', # Optional will default to 'Hiring Manager'
    'cover_letter_file_name': 'cover_letter.pdf', # Optional
    'cover_letter_data': cover_letter_data
}

# Build the file
resi.cover_letter.build_cover_letter_pdf(
    cover_letter_metadata,
    'user_history.json' # can be a file path or a dict
)

```

## Example

To start using resi-builder. First find and copy the job description

<details>
<summary>Job desc sample example</summary>

```text
Science Officer – Exploratory Deep Space Research Vessel

Company: Weyland-Yutani Corporation
Location: Assigned deep space vessel, long-duration mission
Position Type: Full-time, contract assignment
hiring-manager: Mr. Weyland

Overview

Weyland-Yutani seeks a highly skilled Science Officer to join the crew of an exploratory-class deep space research vessel. The Science Officer will serve as the primary advisor on all scientific matters, oversee research initiatives, and ensure mission objectives are met in accordance with corporate and interstellar regulatory standards. This position requires a balance of academic expertise, operational adaptability, and the ability to thrive in isolated, high-stakes environments.

Key Responsibilities

Lead all scientific investigations and research programs aboard the vessel.

Conduct biological, geological, and astrophysical studies relevant to planetary survey missions.

Advise the Captain and corporate stakeholders on scientific risks, opportunities, and mission feasibility.

Oversee the collection, cataloging, and preservation of extraterrestrial samples.

Ensure all scientific protocols and safety procedures are strictly followed.

Collaborate with engineering, medical, and operations officers to integrate scientific findings into mission strategy.

Maintain detailed logs and deliver mission reports to Weyland-Yutani Command.

Qualifications

Ph.D. (or equivalent) in Astrobiology, Exobiology, Astrophysics, or related discipline.

Minimum 5 years of applied research experience, preferably in remote or hazardous environments.

Proven leadership in scientific research teams under constrained conditions.

Strong proficiency in advanced data analysis, laboratory operations, and field methodologies.

Excellent communication skills; ability to present findings clearly to both scientific and corporate audiences.

Preferred Skills

Experience with interstellar survey protocols and first-contact procedures.

Familiarity with AI-assisted research systems and autonomous data collection technologies.

Background in risk assessment for biological and environmental hazards.

Additional Information

Extended assignments (up to 36 months continuous deployment).

Corporate housing and cryosleep accommodations provided.

Compensation and benefits commensurate with the risks and prestige of interstellar exploration.

Loyalty to Weyland-Yutani’s mission of "Building Better Worlds" is essential.
```
</details>

<details>

<summary>User History Example</summary>

```JSON
{
  "contact_info": {
    "name": "Dr. Elena Vasquez",
    "phone": "+1 (555) 392-1847",
    "email": "elena.vasquez@exobio-research.org",
    "linkedIn": "https://www.linkedin.com/in/elena-vasquez-exobio"
  },
  "education": [
    {
      "school": "California Institute of Technology (Caltech)",
      "degree": "Ph.D.",
      "field_of_study": "Astrobiology & Exobiology",
      "location": "Pasadena, CA, USA"
    },
    {
      "school": "University of Cambridge",
      "degree": "M.Sc.",
      "field_of_study": "Astrophysics",
      "location": "Cambridge, UK"
    }
  ],
  "history": [
    {
      "role": "Lead Exobiologist",
      "company": "European Space Agency (ESA) – Titan Life Probe Mission",
      "dates": "2120 – 2125",
      "experience": [
        "Directed on-site biological research during a 4-year mission to Saturn’s moon Titan.",
        "Led the collection and preservation of organic compounds under extreme conditions.",
        "Coordinated with engineering and operations teams to integrate scientific findings into navigation and mission decisions.",
        "Delivered classified mission reports to ESA and UN Interstellar Regulatory Council."
      ],
      "industry": ["Space Exploration", "Exobiology", "Astrobiology"]
    },
    {
      "role": "Senior Research Scientist – Exoplanetary Microbiology",
      "company": "Weyland-Yutani Advanced Research Division",
      "dates": "2115 – 2120",
      "experience": [
        "Led a cross-disciplinary team analyzing microbial extremophiles in simulated exoplanetary environments.",
        "Developed AI-assisted data pipelines for autonomous biological sample classification.",
        "Established safety protocols for extraterrestrial sample containment, reducing contamination risk by 98%.",
        "Contributed to feasibility assessments for multiple exploratory-class vessel missions."
      ],
      "industry": ["Corporate Research", "Space Biotechnology", "Astrobiology"]
    },
    {
      "role": "Astrobiology Research Fellow",
      "company": "NASA Ames Research Center",
      "dates": "2110 – 2115",
      "experience": [
        "Conducted planetary analog studies in Earth’s most extreme deserts and deep-sea environments.",
        "Published 14 peer-reviewed papers on microbial survivability in vacuum and radiation environments.",
        "Served as scientific liaison for mission-planning teams on Mars and Europa exploration programs."
      ],
      "industry": ["Government Research", "Planetary Science", "Biotechnology"]
    }
  ],
  "activities_and_interests": "Deep-sea diving expeditions, xenolinguistics research, mentoring young scientists in interstellar exploration programs, and contributing to open-source AI models for biological pattern recognition.",
  "profile": "Astrobiologist and exobiology expert with over 15 years of applied research experience in remote and hazardous environments. Proven leadership on interstellar missions and deep-space expeditions, with extensive expertise in extraterrestrial sample collection, biological risk assessment, and AI-driven research methodologies. Skilled in bridging scientific insight with operational mission strategy under extreme isolation and high-stakes conditions.",
  "skills": [
    "Astrobiology",
    "Exobiology",
    "Exoplanetary Microbiology",
    "Risk Assessment",
    "Scientific Leadership",
    "AI-Assisted Data Analysis",
    "Planetary Survey Protocols",
    "Extraterrestrial Sample Preservation",
    "Mission Report Writing",
    "Cross-disciplinary Collaboration"
  ]
}

```

</details>

### Resume

Sample code

```python
import resi

# import the job desc from a text file
with open('job_desc.txt', 'r') as f:
    job_desc = f.read()

# Job metadata
metadata = {
    'job_desc': job_desc,
}

# Build the preview data - output will be a python dictionary
resume_data =  resi.resume.build_resume_preview(
    metadata,
    'user_history.json', # Importing a file via file path
)
```

<details>

  <summary>Preview output</summary>

  ```JSON
{
    "profile": "Astrobiologist and exobiology expert with over 15 years of applied research\\nexperience in remote and hazardous environments. Proven leadership on\\ninterstellar missions and deep-space expeditions, with extensive expertise in\\nextraterrestrial sample collection, biological risk assessment, and AI-driven\\nresearch methodologies. Skilled in bridging scientific insight with operational\\nmission strategy under extreme isolation and high-stakes conditions.",
    "bullets": [
        {
            "role": "Lead Exobiologist",
            "company": "European Space Agency (ESA) \\u2013 Titan Life Probe Mission",
            "dates": "2120 \\u2013 2125",
            "experience": ["Directed biological research during a four-year mission to Saturn\'s moon Titan supporting planetary survey objectives.",
                "Led the collection and preservation of extraterrestrial organic compounds under extreme environmental conditions.",
                "Collaborated with engineering and operations teams to integrate scientific findings into mission decision-making processes.",
                "Delivered comprehensive mission reports to ESA and interstellar regulatory bodies, supporting compliance and data sharing.",
                "Conducted biological investigations aligned with planetary exploration and extraterrestrial sample handling protocols."
            ]
        },
        {
            "role": "Senior Research Scientist \\u2013 Exoplanetary Microbiology",
            "company": "Weyland-Yutani Advanced Research Division",
            "dates": "2115 \\u2013 2120",
            "experience": [
                "Led a team analyzing microbial extremophiles in simulated exoplanetary environments to assess habitability for planetary surveys.",
                "Developed AI-assisted data pipelines for autonomous classification of extraterrestrial biological samples.",
                "Established safety and containment protocols for extraterrestrial sample management enhancing mission safety standards.",
                "Contributed to feasibility studies for exploratory vessel missions focusing on biological risks and planetary conditions.",
                "Applied microbiology expertise to support interstellar exploration and extraterrestrial biological assessments."
            ]
        },
        {
            "role": "Astrobiology Research Fellow",
            "company": "NASA Ames Research Center",
            "dates": "2110 \\u2013 2115",
            "experience": ["Conducted planetary analog research in Earth\'s extreme desert and deep-sea environments simulating extraterrestrial conditions.",
                "Authored peer-reviewed publications on microbial survivability in vacuum and radiation environments relevant to space missions.",
                "Served as scientific liaison for Mars and Europa exploration planning, integrating biological studies into mission concepts.",
                "Performed biological fieldwork supporting planetary survey protocols and environmental hazard assessments.",
                "Contributed to the development of safety and contamination prevention strategies in biological field research."
            ]
        }
    ],
    "skills": [
        "Astrobiology",
        "Exobiology",
        "Exoplanetary Microbiology",
        "Risk Assessment",
        "Scientific Leadership",
        "AI-Assisted Data Analysis",
        "Planetary Survey Protocols",
        "Extraterrestrial Sample Preservation",
        "Mission Report Writing",
        "Cross-disciplinary Collaboration"
    ]
}
  ```
</details>


Now, to build the resume pdf file.

```python
# resume_metadata
resume_metadata = {
    'resume_file_name': 'resume.pdf',
    'resume_data': resume_data
}

# Build the file
resi.resume.build_resume_pdf(
    resume_metadata,
    'user_history.json'
)
```

![resume_first_page](/data/imgs/resume.jpg)
![resume_first_page2](/data/imgs/resume2.jpg)


### Cover Letter

Sample Code

```python
# import the job desc from a text file
with open('job_desc.txt', 'r') as f:
    job_desc = f.read()

# Job metadata
metadata = {
    'job_desc': job_desc,
    'cover_letter_file_name': 'cover_letter.pdf'
}

# Build the preview data - output will be a python dictionary
cover_letter_data =  resi.cover_letter.build_cover_letter_preview(
    metadata,
    'user_history.json', # Importing a file via file path
)
```

<details>

  <summary>Preview output</summary>

  ```JSON
{
    "intro": "Dear Mr. Weyland,",
    "paragraphs": {
        "0": "I am excited to apply for the position of Science Officer aboard your exploratory deep space research vessel. With a Ph.D. in Astrobiology and Exobiology from Caltech, as well as a Master\'s degree in Astrophysics from the University of Cambridge, I have developed a strong foundation in planetary sciences and biological research in extreme environments. My over 15 years of experience in space exploration and exobiology, including leading biological research during a four-year mission to Saturn\\u2019s moon Titan with the European Space Agency, aligns well with the responsibilities of this role.",
        "1": "Throughout my career, I have led scientific investigations focused on extraterrestrial sample collection, preservation, and analysis, ensuring rigorous safety protocols are maintained in hazardous conditions. I have coordinated closely with engineering and operations teams to integrate scientific findings into mission strategies, similar to the interdisciplinary collaboration required on your vessel. My experience in developing AI-assisted data pipelines to automate biological sample classification demonstrates my ability to leverage advanced technologies in remote environments. Additionally, my work at Weyland-Yutani as a Senior Research Scientist involved conducting microbial extremophile studies in simulated exoplanetary environments and establishing containment protocols to minimize environmental risks.",
        "2": "I am confident that my background in astrobiology, experience in planetary survey protocols, and proven leadership in scientific research teams under constrained conditions will contribute significantly to the success of your mission. My extensive documentation of scientific findings and ability to communicate complex data clearly to diverse audiences will support Weyland-Yutani\'s objectives of building better worlds through pioneering exploration."
    }
}
  ```
</details>

Now to build the cover letter file

```python
# cover letter metadata
cover_letter_metadata = {
    'hiring_manager': 'Mr. Weyland',
    'cover_letter_file_name': 'cover_letter.pdf',
    'cover_letter_data': cover_letter_data
}

# Build the file
resi.cover_letter.build_cover_letter_pdf(
    cover_letter_metadata,
    'user_history.json'
)
```

![cover_letter](/data/imgs/cover_letter.jpg)