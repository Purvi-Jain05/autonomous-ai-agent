from fastapi import FastAPI

from api.routes import router


app = FastAPI(
    title="Autonomous AI Agent",
    version="1.0"
)

app.include_router(router)