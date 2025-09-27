from pydantic import BaseModel
from datetime import datetime
from typing import List, Optional, Dict

class FinancialData(BaseModel):
    statement_type: str
    period: datetime
    data: Dict[str, float]

class FinancialRatioResult(BaseModel):
    ratio_name: str
    ratio_value: float

class HealthScoreResult(BaseModel):
    score: float
    factors: Dict[str, float]

class AnalysisRequest(BaseModel):
    company_id: int
    periods: List[datetime]  # Data for multiple periods

class AnalysisResponse(BaseModel):
    ratios: List[FinancialRatioResult]
    health_score: HealthScoreResult