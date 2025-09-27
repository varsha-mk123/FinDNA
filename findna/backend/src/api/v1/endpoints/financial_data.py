from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from ...core.database import get_db
from ...models.database_models import FinancialStatement, FinancialRatio, HealthScore
from ...models.api_schemas import FinancialData, AnalysisRequest, AnalysisResponse
from ...services.financial_analysis.dna_mapper import DNAMapper
from ...services.financial_analysis.health_scorer import HealthScorer

router = APIRouter()

@router.post("/upload", response_model=dict)
async def upload_financial_data(data: FinancialData, db: Session = Depends(get_db)):
    # Save financial statement to database
    statement = FinancialStatement(
        company_id=1,  # Hardcoded for now, would come from auth
        statement_type=data.statement_type,
        period=data.period,
        data=str(data.data)  # In production, use a JSON field
    )
    db.add(statement)
    db.commit()
    
    return {"message": "Data uploaded successfully"}

@router.post("/analyze", response_model=AnalysisResponse)
async def analyze_financials(request: AnalysisRequest, db: Session = Depends(get_db)):
    # In a real scenario, we would fetch the financial data for the given company and periods
    # For now, we'll use dummy data
    dummy_data = {
        'current_assets': 100000,
        'current_liabilities': 50000,
        'total_liabilities': 200000,
        'total_equity': 300000,
        'net_income': 50000,
        'total_assets': 500000
    }
    
    dna_mapper = DNAMapper()
    ratios_dict = dna_mapper.calculate_ratios(dummy_data)
    
    # Convert to list of FinancialRatioResult
    ratios = [{"ratio_name": k, "ratio_value": v} for k, v in ratios_dict.items()]
    
    health_scorer = HealthScorer()
    health_score_result = health_scorer.calculate_score(ratios_dict)
    
    return AnalysisResponse(
        ratios=ratios,
        health_score=health_score_result
    )