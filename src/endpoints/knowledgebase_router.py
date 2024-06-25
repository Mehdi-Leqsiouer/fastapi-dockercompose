"""Module for the knowledge base endpoints"""
from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from src.schemas.knowledgebase import KnowledgebaseGet
from src.services.knowledgebase import KnowledgebaseService
from src.settings.db import get_db

router = APIRouter()


@router.get("/kb/", response_model=List[KnowledgebaseGet], tags=["kb_ops"])
async def get_kb(db: Session = Depends(get_db)) -> List[KnowledgebaseGet]:
    """
    # KB endpoint to list all the KB rows
    Get all kb data
    Arguments:
    ----------
        None
    Returns:
    ----------
        List[KnowledgebaseGet]: list of rows inside the kb
    """
    try:
        return KnowledgebaseService.get_all_knowledgebases(db)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) from e
