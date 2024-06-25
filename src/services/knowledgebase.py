"""Module for interfacing with KB models"""
from typing import List, Union

from fastapi import HTTPException

from src.models.knowledgebase import KnowledgeBase
from src.settings.logger import DEFAULT_LOGGER


class KnowledgebaseService:
    """Service for knowledgebase"""

    @classmethod
    def get_all_knowledgebases(cls, db) -> Union[List[KnowledgeBase], HTTPException]:
        """
        Get all existing knowledgebase.

        Arguments:
        ----------
            db (Session): Database session.

        Returns
        -------
            List[Program]: List of knowledgebase data.
        """
        try:
            return db.query(KnowledgeBase).all()
        except Exception as e:
            detail = f"An error occured while retrieving the programs: {e}"
            DEFAULT_LOGGER.info(detail)
            raise HTTPException(
                status_code=400,
                detail=detail,
            ) from e
