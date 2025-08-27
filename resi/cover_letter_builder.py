from reportlab.lib.pagesizes import LETTER
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from .open_ai_writer import cover_letter_generator
from .utils import pdf_utils


def build_cover_letter_preview(metadata: dict, history: dict) -> dict:
    """
    Build a Cover Letter preview that is ready for review
    """

    # Step 1: Generate initial cover letter text
    body = cover_letter_generator(metadata, history)

    # Step 2: Write it to a temp text file for approval
    paragraphs = body.strip().split("\n\n")

    # Step 3: return the file for preview
    body = {
        'intro': f"Dear {metadata['hiring_manager']},",
        'paragraphs': {k:v for k,v in enumerate(paragraphs)},
    }

    return body


def build_cover_letter_final(body, user_history):
    """
    Build the final pdf file
    """

    # Remove any spaces at the end
    paragraphs = [x.strip() for x in body['cover_letter_data']['paragraphs'].values()]

    # Build the PDF
    doc = SimpleDocTemplate(body['cover_letter_file_name'], pagesize=LETTER, rightMargin=36, leftMargin=36, topMargin=36, bottomMargin=24)
    Story = []

    styles = pdf_utils.get_styles()
    # Add name title
    pdf_utils.add_name_header(Story, styles, user_history['contact_info']['name'])
    # Add info bar
    pdf_utils.add_info_bar(Story, styles, [x for x in user_history['contact_info'].values()])

    # Greeting
    Story.append(Paragraph(f"Dear {body['hiring_manager']},", styles['CustomBodyText']))
    Story.append(Spacer(1, 12))  # Paragraph break

    # Paragraph section
    for para in paragraphs:
        Story.append(Paragraph(para, styles['CustomBodyText']))
        Story.append(Spacer(1, 12))  # Paragraph break

    # Sign off
    Story.append(Paragraph(f"Sincerely<br/>{'Mario Cerda'}", styles['CustomBodyText']))

    doc.build(Story)
    print(f"Cover letter generated: {body['cover_letter_file_name']}")

    
