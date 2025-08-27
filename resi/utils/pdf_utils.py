from reportlab.lib.pagesizes import LETTER
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import Paragraph, Spacer, HRFlowable

def get_styles():
    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(
        name='Header',
        fontSize=12,
        leading=14,
        spaceAfter=10,
        spaceBefore=10,
        leftIndent=0,
        fontName='Helvetica-Bold'
    ))
    styles.add(ParagraphStyle(
        name='CustomBodyText',
        fontSize=10,
        leading=12
    ))
    styles.add(ParagraphStyle(
        name='CustomBullet',
        fontSize=10,
        leftIndent=20,
        bulletIndent=10,
        spaceAfter=2
    ))
    styles.add(ParagraphStyle(
        name='NameHeading',
        fontSize=20,
        leading=24,
        spaceAfter=6,
        spaceBefore=0,
        alignment=1,
        fontName='Helvetica-Bold'
    ))
    styles.add(ParagraphStyle(
        name='CenteredText',
        fontSize=10,
        leading=12,
        alignment=1
    ))
    return styles

def add_section(story, title, styles, content=None, bullets=None, spacer_height=1):
    story.append(Paragraph(f"<b>{title}</b>", styles['Header']))
    if content:
        story.append(Paragraph(content, styles['CustomBodyText']))
    if bullets:
        for bullet in bullets:
            story.append(Paragraph(f"• {bullet}", styles['CustomBullet']))
    story.append(Spacer(1, spacer_height))


def add_name_header(story, styles, content):
    story.append(Paragraph(content, styles['NameHeading']))


def add_info_bar(story, styles, content: list[str]):
    story.append(Spacer(1, 4))
    story.append(HRFlowable(width="100%", thickness=1, color="#000000", spaceBefore=4, spaceAfter=8))

    # Build the info bar from content dynamically
    info_bar = " | ".join(content)

    story.append(Paragraph(info_bar, styles['CenteredText']))
    story.append(Spacer(1, 20))
