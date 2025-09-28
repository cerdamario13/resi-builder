import resi

def test_cover_letter_preview():
    """
    Test that the preview is working
    """

    # import the job desc from a text file
    with open('data/test_data/job_desc.txt', 'r') as f:
        job_desc = f.read()

    # Build the preview data - output will be a python dictionary
    cover_letter_data =  resi.cover_letter.build_cover_letter_preview(
        job_desc,
        'data/test_data/user_history.json', # Importing a file via file path
    )

    assert list(cover_letter_data.keys()) == ['intro', 'paragraphs']

def test_cover_letter_preview_additional_prompts():
    """
    Test that the preview is working
    """

    # import the job desc from a text file
    with open('data/test_data/job_desc.txt', 'r') as f:
        job_desc = f.read()

    # Build the preview data - output will be a python dictionary
    cover_letter_data =  resi.cover_letter.build_cover_letter_preview(
        job_desc,
        'data/test_data/user_history.json', # Importing a file via file path
        None,
        'Translate to Spanish'
    )

    assert list(cover_letter_data.keys()) == ['intro', 'paragraphs']

def test_cover_letter_pdf():
    """
    Test the generation of the pdf file
    """

    # Mocked cover_letter_data
    cover_letter_data = {
        "intro": "Dear Mr. Weyland,",
        "paragraphs": {
            "0": "I am excited to apply for the position of Science Officer aboard your exploratory deep space research vessel. With a Ph.D. in Astrobiology and Exobiology from Caltech, as well as a Master\'s degree in Astrophysics from the University of Cambridge, I have developed a strong foundation in planetary sciences and biological research in extreme environments. My over 15 years of experience in space exploration and exobiology, including leading biological research during a four-year mission to Saturn\\u2019s moon Titan with the European Space Agency, aligns well with the responsibilities of this role.",
            "1": "Throughout my career, I have led scientific investigations focused on extraterrestrial sample collection, preservation, and analysis, ensuring rigorous safety protocols are maintained in hazardous conditions. I have coordinated closely with engineering and operations teams to integrate scientific findings into mission strategies, similar to the interdisciplinary collaboration required on your vessel. My experience in developing AI-assisted data pipelines to automate biological sample classification demonstrates my ability to leverage advanced technologies in remote environments. Additionally, my work at Weyland-Yutani as a Senior Research Scientist involved conducting microbial extremophile studies in simulated exoplanetary environments and establishing containment protocols to minimize environmental risks.",
            "2": "I am confident that my background in astrobiology, experience in planetary survey protocols, and proven leadership in scientific research teams under constrained conditions will contribute significantly to the success of your mission. My extensive documentation of scientific findings and ability to communicate complex data clearly to diverse audiences will support Weyland-Yutani\'s objectives of building better worlds through pioneering exploration."
        }
    }

    # Build the file
    resi.cover_letter.build_cover_letter_pdf(
        cover_letter_data,
        'data/test_data/user_history.json',
        'data/test_data/output_files/cover_letter'
    )

