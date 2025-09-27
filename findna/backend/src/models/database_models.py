from sqlalchemy import Column, Integer, String, Float, DateTime, Text
from sqlalchemy.sql import func
from ..core.database import Base

class FinancialStatement(Base):
    __tablename__ = "financial_statements"

    id = Column(Integer, primary_key=True, index=True)
    company_id = Column(Integer, index=True)
    statement_type = Column(String)  # 'income_statement', 'balance_sheet', 'cash_flow'
    period = Column(DateTime)
    data = Column(Text)  # JSON string of the statement data

class FinancialRatio(Base):
    __tablename__ = "financial_ratios"

    id = Column(Integer, primary_key=True, index=True)
    company_id = Column(Integer, index=True)
    period = Column(DateTime)
    ratio_name = Column(String)
    ratio_value = Column(Float)

class HealthScore(Base):
    __tablename__ = "health_scores"

    id = Column(Integer, primary_key=True, index=True)
    company_id = Column(Integer, index=True)
    period = Column(DateTime)
    score = Column(Float)  # 0-100
    factors = Column(Text)  # JSON string of factors affecting the score