import resi

def test_resume_preview():
    """
    Test the resume preview
    """
    # import the job desc from a text file
    with open('data/test_data/job_desc.txt', 'r') as f:
        job_desc = f.read()

    # Build the preview data - output will be a python dictionary
    resume_data =  resi.resume.build_resume_preview(
        job_desc,
        'data/test_data/user_history.json', # Importing a file via file path
    )

    assert list(resume_data.keys()) == ['profile', 'bullets', 'skills']

def test_resume_preview_with_additional_messages():
    """
    Test the resume preview
    """
    # import the job desc from a text file
    with open('data/test_data/job_desc.txt', 'r') as f:
        job_desc = f.read()

    # Build the preview data - output will be a python dictionary
    resume_data =  resi.resume.build_resume_preview(
        job_desc,
        'data/test_data/user_history.json', # Importing a file via file path
        'Translate output to Spanish'
    )
    
    assert list(resume_data.keys()) == ['profile', 'bullets', 'skills']

def test_cover_letter_pdf():
    """
    Test the generation of the pdf file
    """

    # resume data mock
    resume_data = {
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

    # resume_metadata
    resume_metadata = {
        'resume_file_name': 'data/test_data/output_files/resume.pdf',
        'resume_data': resume_data
    }

    # Build the file
    resi.resume.build_resume_pdf(
        resume_metadata,
        'data/test_data/user_history.json'
    )
