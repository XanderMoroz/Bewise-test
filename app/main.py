import uvicorn
from fastapi import FastAPI

from app.core.config import settings
from app.api.endpoints import quiz


app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION,
    description=settings.DESCRIPTION,
    openapi_url="/openapi.json",
    docs_url="/",)

app.include_router(quiz.router, tags=["questions"])


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)