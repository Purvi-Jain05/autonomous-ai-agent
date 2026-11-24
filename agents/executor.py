from llm.llm_manager import LLMManager
from utils.logger import logger


class Executor:

    def __init__(self):

        self.llm = LLMManager()

    def execute_tasks(
        self,
        user_request: str,
        tasks: list
    ):

        document = {}

        provider_used = ""

        total = len(tasks)

        logger.info(
            f"Executing {total} Sections..."
        )

        for index, heading in enumerate(tasks, start=1):

            logger.info(
                f"[{index}/{total}] {heading}"
            )

            prompt = f"""
You are an expert Business Proposal Writer.

Generate ONLY the section below.

Project Request:
{user_request}

Section Title:
{heading}

Instructions:

- Write between 180-250 words.
- Use professional business language.
- Be detailed.
- Do not repeat previous sections.
- Do not generate any title except this section.
- Return plain text only.
"""

            response, provider = self.llm.generate(prompt)

            provider_used = provider

            document[heading] = response.strip()

            logger.success(
                f"{heading} Completed"
            )

        logger.success(
            "Execution Completed"
        )

        return document, provider_used