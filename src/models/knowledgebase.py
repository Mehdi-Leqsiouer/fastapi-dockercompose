"""Table KB model"""
from sqlalchemy import Column, Integer, String

from src.models.declarative_base import Base


class KnowledgeBase(Base):
    """
    Knowledgebase model
    """

    __tablename__ = "knowledgebase"

    kb_row_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    vendor = Column("Vendor", String(50))
    ct_version = Column("CT Version", String(50))
    test_domain = Column("Test Domain", String(50))
    vendor_test_code = Column("Vendor Test Code", String(100))
    vendor_test_name = Column("Vendor Test Name", String(100))
    vendor_specimen = Column("Vendor Specimen", String(100), default=None)
    vendor_method = Column("Vendor Method", String(100), default=None)
    vendor_category = Column("Vendor Category", String(100), default=None)
    vendor_unit = Column("Vendor Unit", String(100), default=None)
    sanofi_test_code = Column("Sanofi Test Code", String(50), default=None)
    sanofi_test_name = Column("Sanofi Test Name", String(50), default=None)
    sanofi_specimen = Column("Sanofi Specimen", String(100), default=None)
    sanofi_method = Column("Sanofi Method", String(100), default=None)
    sanofi_category = Column("Sanofi Category", String(100), default=None)
    sanofi_unit = Column("Sanofi Unit", String(100), default=None)
    comments = Column("Comments", String(500), default=None)
