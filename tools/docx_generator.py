from docx import Document
from docx.shared import Pt
from docx.enum.text import WD_PARAGRAPH_ALIGNMENT

from datetime import datetime
import os

from config import config
from utils.logger import logger


class DocxGenerator:

    def __init__(self):

        os.makedirs(
            config.OUTPUT_DIR,
            exist_ok=True
        )

    def generate(
        self,
        document_data: dict,
        filename="generated_document.docx"
    ):

        try:

            document = Document()

            # -----------------------------
            # Title
            # -----------------------------
            title = document.add_heading(
                "AI Generated Project Proposal",
                level=1
            )

            title.alignment = WD_PARAGRAPH_ALIGNMENT.CENTER

            title.runs[0].font.size = Pt(22)

            # -----------------------------
            # Date
            # -----------------------------
            date_para = document.add_paragraph()

            date_para.alignment = WD_PARAGRAPH_ALIGNMENT.CENTER

            date_para.add_run(
                f"Generated On : {datetime.now().strftime('%d %B %Y %I:%M %p')}"
            ).italic = True

            document.add_paragraph()

            # -----------------------------
            # Sections
            # -----------------------------
            for heading, content in document_data.items():

                heading_para = document.add_heading(
                    heading,
                    level=2
                )

                heading_para.runs[0].font.size = Pt(16)

                paragraph = document.add_paragraph()

                paragraph.style = "Normal"

                run = paragraph.add_run(content)

                run.font.size = Pt(11)

                document.add_paragraph()

            # -----------------------------
            # Save
            # -----------------------------
            file_path = os.path.join(
                config.OUTPUT_DIR,
                filename
            )

            document.save(file_path)

            logger.success(
                f"Document Saved : {file_path}"
            )

            return file_path

        except PermissionError:

            logger.error(
                "Please close the Word document and try again."
            )

            raise Exception(
                "Permission Denied. Close the Word document before generating a new one."
            )

        except Exception as e:

            logger.error(str(e))

            raise