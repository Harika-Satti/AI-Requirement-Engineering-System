from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph
)

from reportlab.lib.styles import getSampleStyleSheet

import os


def generate_pdf(content, filename):

    os.makedirs(
        "exports",
        exist_ok=True
    )

    filepath = f"exports/{filename}.pdf"

    pdf = SimpleDocTemplate(filepath)

    styles = getSampleStyleSheet()

    elements = [
        Paragraph(content, styles["Normal"])
    ]

    pdf.build(elements)

    return filepath