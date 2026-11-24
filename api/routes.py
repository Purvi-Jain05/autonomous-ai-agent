import time

from fastapi import APIRouter, HTTPException

from models.request import AgentRequest
from models.response import AgentResponse

from agents.planner import Planner
from agents.executor import Executor

from tools.docx_generator import DocxGenerator

from utils.logger import logger

router = APIRouter()

planner = Planner()
executor = Executor()
generator = DocxGenerator()


@router.post(
    "/agent",
    response_model=AgentResponse
)
def run_agent(data: AgentRequest):

    start_time = time.time()

    try:

        logger.info("New Request Received")

        tasks, planner_llm = planner.create_plan(
            data.request
        )

        document, executor_llm = executor.execute_tasks(
            data.request,
            tasks
        )

        file_path = generator.generate(
            document
        )

        execution_time = round(
            time.time() - start_time,
            2
        )

        logger.success(
            f"Completed in {execution_time} sec"
        )

        return AgentResponse(

            status="success",

            message="Document generated successfully.",

            tasks=tasks,

            document=file_path,

            llm_used=executor_llm,

            execution_time=execution_time

        )

    except Exception as e:

        logger.exception(e)

        execution_time = round(
            time.time() - start_time,
            2
        )

        return AgentResponse(

            status="error",

            message=str(e),

            execution_time=execution_time

        )