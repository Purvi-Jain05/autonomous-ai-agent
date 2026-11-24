import json
import re

from llm.llm_manager import LLMManager
from utils.logger import logger


class Planner:

    def __init__(self):

        self.llm = LLMManager()

    def create_plan(self, user_request: str):

        prompt = f"""
You are an expert AI Project Planner.

Your job is to create a HIGH-LEVEL plan for the user's request.

User Request:
{user_request}

Instructions:

- Return ONLY a JSON array.
- Return exactly 8 major section headings.
- Do NOT generate explanations.
- Do NOT generate paragraphs.
- Do NOT use markdown.
- Do NOT number the items.

Example Output:

[
    "Executive Summary",
    "Problem Statement",
    "Proposed Solution",
    "Key Features",
    "Technology Stack",
    "Implementation Timeline",
    "Benefits & Impact",
    "Conclusion"
]
"""

        response, provider = self.llm.generate(prompt)

        logger.info(f"Planner used : {provider}")

        try:

            match = re.search(
                r"\[.*\]",
                response,
                re.DOTALL
            )

            if match:

                tasks = json.loads(match.group())

            else:

                raise Exception("No JSON Found")

            logger.success(
                f"{len(tasks)} Tasks Generated"
            )

            return tasks, provider

        except Exception as e:

            logger.error("Planner Parsing Failed")

            logger.error(str(e))

            fallback_tasks = [

                "Executive Summary",

                "Problem Statement",

                "Proposed Solution",

                "Key Features",

                "Technology Stack",

                "Implementation Timeline",

                "Benefits & Impact",

                "Conclusion"

            ]

            return fallback_tasks, provider