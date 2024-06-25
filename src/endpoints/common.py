"""Module containing common endpoints"""

import os

from fastapi import APIRouter
from fastapi.responses import HTMLResponse, JSONResponse

router = APIRouter()
env = os.environ["CURRENT_ENVIRONMENT"]


@router.get("/", tags=["common"])
def read_root() -> HTMLResponse:
    """
    # Common endpoint documentation
    This endpoint returns an HTML page wiht a link to the Swagger documentation"""
    return HTMLResponse(
        f"Welcome in the API. ENV : {env} "
        "Go to <a href='/docs'>/docs</a> to see the documentation of the API"
    )


@router.get("/health", tags=["common"])
async def health_check() -> JSONResponse:
    """
    # Common endpoint health check
    Returns OK if the health of the api is OK"""
    return JSONResponse(content={"status": "ok"})
