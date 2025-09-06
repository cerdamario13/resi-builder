from reportlab.lib.pagesizes import LETTER
from reportlab.platypus import SimpleDocTemplate, Spacer, Table, TableStyle
from reportlab.lib import colors
from .open_ai_writer import generate_job_bullets
from .utils import pdf_utils
import textwrap
from typing import Union
import json
import copy
import os

def build_resume_preview(job_metadata: dict, user_history: Union[str, dict]) -> dict:
    """
    Build resume data preview dictionary.

    :param job_metadata: Job related dictionary that includes hiring_manager, job_description and additional_messages
    :param user_history: Either a dictionary of the user's resume work history,
                         or a path to a JSON file containing that dictionary.
    :return: Resume preview dictionary
    """

    # Normalize input: if user_history is a str, load JSON file
    if isinstance(user_history, str):
        with open(user_history, "r") as f:
            user_history = json.load(f)

    user_history_copy = copy.deepcopy(user_history)

    # Delete the contact info to avoid passing personal data to the LLM except for name
    del user_history_copy['contact_info']
    user_history_copy['contact_info'] = {'name': user_history['contact_info']['name']}

    # Step 1: Generate initial resume content
    wrapped_profile = textwrap.fill(user_history_copy['profile'].strip(), width=80)

    # bullet points
    bullets = generate_job_bullets(job_metadata, user_history_copy)

    # skills
    skills = user_history_copy['skills']

    # Step 2: Build preview dictionary
    body = {
        'profile': wrapped_profile,
        'bullets': bullets,
        'skills': skills,
    }

    return body

def build_resume_pdf(body: dict, user_history: Union[str, dict]) -> None:
    """
    Build the resume as a pdf file

    :param body: resume body as a dictionary
    :param user_history: Either a dictionary of the user's resume work history,
                         or a path to a JSON file containing that dictionary.
    :return: PDF resume file
    """

    # Normalize input: if user_history is a str, load JSON file
    if isinstance(user_history, str):
        with open(user_history, "r") as f:
            user_history = json.load(f)

    # Check if there is a file name provided and normalize to pdf
    file_name = body.get('resume_file_name', 'resume.pdf')
    base, ext = os.path.splitext(file_name)
    if ext.lower() != '.pdf':
        file_name = f"{base}.pdf"

    # Build the PDF
    doc = SimpleDocTemplate(file_name, pagesize=LETTER, rightMargin=36, leftMargin=36, topMargin=36, bottomMargin=24)
    Story = []

    styles = pdf_utils.get_styles()

    # Add name title
    pdf_utils.add_name_header(Story, styles, user_history['contact_info']['name'])

    pdf_utils.add_info_bar(Story, styles, [x for x in user_history['contact_info'].values()])

    # Profile
    pdf_utils.add_section(Story, "Profile", styles, content=body['resume_data']['profile'])

    # Experience
    pdf_utils.add_section(Story, "Experience", styles)
    for exp in body['resume_data']['bullets']:
        pdf_utils.add_section(
            Story,
            f"{exp['role'].upper()} | {exp['company'].upper()} | {exp['dates'].upper()}",
            styles,
            bullets=exp['experience']
        )

    # Education
    for education in user_history['education']:
            pdf_utils.add_section(story=Story, title=f"{education['degree'].upper()} IN {education['field_of_study'].upper()} | {education['school'].upper()}, {education['location'].upper()}", styles=styles)

    # Skills

    # Make sure number of skills is even (pad if needed)
    if len(body['resume_data']['skills']) % 2 != 0:
        body['resume_data']['skills'].append("")

    half = len(body['resume_data']['skills']) // 2
    data = list(zip(
        [f"• {skill}" for skill in body['resume_data']['skills'][:half]],
        [f"• {skill}" if skill else '' for skill in body['resume_data']['skills'][half:]] # ensure that the last value is not displayed if empty
    ))

    table = Table(data, colWidths=[250, 250])  # Adjust widths as needed

    table.setStyle(TableStyle([
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('LEFTPADDING', (0, 0), (-1, -1), 4),
        ('RIGHTPADDING', (0, 0), (-1, -1), 4),
        ('FONTSIZE', (0, 0), (-1, -1), 10),
        ('TEXTCOLOR', (0, 0), (-1, -1), colors.black),
    ]))

    pdf_utils.add_section(story=Story, title="Skills & Abilities", styles=styles)
    Story.append(table)
    Story.append(Spacer(1, 2))

    # Activities
    pdf_utils.add_section(story=Story, title="Activities and Interests", styles=styles, content=f"{user_history['activities_and_interests']}")

    # Build PDF
    doc.build(Story)
    print(f"Resume generated: {file_name}")
