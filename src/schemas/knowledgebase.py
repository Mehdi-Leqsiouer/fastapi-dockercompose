"""Module for knowledge base schema"""
from typing import List, Optional

from pydantic import BaseModel


class KnowledgebaseGet(BaseModel):
    """Knowledgebase schema GEt"""

    kb_row_id: int
    vendor: str
    ct_version: str
    test_domain: str
    vendor_test_code: str
    vendor_test_name: str
    vendor_specimen: Optional[str]
    vendor_method: Optional[str]
    vendor_category: Optional[str]
    vendor_unit: Optional[str]
    sanofi_test_code: Optional[str]
    sanofi_test_name: Optional[str]
    sanofi_specimen: Optional[str]
    sanofi_method: Optional[str]
    sanofi_category: Optional[str]
    sanofi_unit: Optional[str]
    comments: Optional[str]
    termsprogress_row_id: Optional[int]

    class Config:
        """ORM Config"""

        orm_mode = True


class KnowledgebasePost(BaseModel):
    """Knowledgebase schema Post"""

    vendor: str
    ct_version: str
    test_domain: str
    vendor_test_code: str
    vendor_test_name: str
    vendor_specimen: Optional[str]
    vendor_method: Optional[str]
    vendor_category: Optional[str]
    vendor_unit: Optional[str]
    sanofi_test_code: Optional[str]
    sanofi_test_name: Optional[str]
    sanofi_specimen: Optional[str]
    sanofi_method: Optional[str]
    sanofi_category: Optional[str]
    sanofi_unit: Optional[str]
    comments: Optional[str]
    termsprogress_row_id: Optional[int]

    class Config:
        """ORM Config"""

        orm_mode = True


class KnowledgebasePatch(BaseModel):
    """Knowledgebase schema Patch"""

    vendor: Optional[str]
    ct_version: Optional[str]
    test_domain: Optional[str]
    vendor_test_code: Optional[str]
    vendor_test_name: Optional[str]
    vendor_specimen: Optional[str]
    vendor_method: Optional[str]
    vendor_category: Optional[str]
    vendor_unit: Optional[str]
    sanofi_test_code: Optional[str]
    sanofi_test_name: Optional[str]
    sanofi_specimen: Optional[str]
    sanofi_method: Optional[str]
    sanofi_category: Optional[str]
    sanofi_unit: Optional[str]
    comments: Optional[str]
    termsprogress_row_id: Optional[int]

    class Config:
        """ORM Config"""

        orm_mode = True


class KnowledgebaseParams(BaseModel):
    """Knowledgebase schema Params"""

    vendors: List[str]
    ct_versions: List[str]

    class Config:
        """ORM Config"""

        orm_mode = True
