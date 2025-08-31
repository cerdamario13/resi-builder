from reportlab.lib.pagesizes import LETTER
from reportlab.platypus import SimpleDocTemplate, Spacer, Table, TableStyle
from reportlab.lib import colors
from .open_ai_writer import generate_job_bullets
from .utils import pdf_utils
import textwrap

def build_resume_preview(job_metadata: dict, user_history: dict) -> dict:
    """
    Build resume data preview dictionary.

    :param job_metadata: Job related dictionary that includes hiring_manager, job_description and additional_messages
    :param user_history: Dictionary of the user's resume work history
    """

    # Step 1: Generate initial resume content
    wrapped_profile = textwrap.fill(user_history['profile'].strip(), width=80)

    # bullet points
    bullets = generate_job_bullets(job_metadata, user_history)

    # skills
    skills = user_history['skills']

    # Step 2: Write content to temp json file for approval

    body = {
        'profile': wrapped_profile,
        'bullets': bullets,
        'skills': skills,
    }

    # Step 3: Return the file for review
    return body

def build_resume_pdf(body: dict, user_history: dict):
    """
    Build the resume as a pdf file
    """

    # Build the PDF
    doc = SimpleDocTemplate(body['resume_file_name'], pagesize=LETTER, rightMargin=36, leftMargin=36, topMargin=36, bottomMargin=24)
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
    print(f"Resume generated: {body['resume_file_name']}")
