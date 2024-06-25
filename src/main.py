"""Main module"""

from fastapi import FastAPI
from sqlalchemy.exc import OperationalError
from starlette.middleware.cors import CORSMiddleware

from src.endpoints.common import router as common_router
from src.endpoints.knowledgebase_router import router as kb_router
from src.models.declarative_base import Base
from src.settings.db import engine

origins = ["*"]


app = FastAPI()
try:
    Base.metadata.create_all(bind=engine)
except OperationalError:
    pass

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(common_router)
app.include_router(kb_router)
