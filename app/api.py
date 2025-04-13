from fastapi import APIRouter, Depends, HTTPException, Query
from typing import Optional
from sqlalchemy.orm import Session
from datetime import datetime
from app.database import get_db
from app.schemas import DeviceStatisticCreate, AnalysisResponse
from app.repository import DeviceStatisticRepository

router = APIRouter()

@router.post("/statistics", response_model=DeviceStatisticCreate)
def create_statistic(stat: DeviceStatisticCreate, db: Session = Depends(get_db)):
    repo = DeviceStatisticRepository(db)
    created_stat = repo.create_statistic(stat)
    return created_stat

@router.get("/statistics/device/{device_id}", response_model=AnalysisResponse)
def get_device_statistics(
    device_id: str,
    start: Optional[datetime] = Query(None, description="Начало интервала (ISO8601)"),
    end: Optional[datetime] = Query(None, description="Конец интервала (ISO8601)"),
    db: Session = Depends(get_db)
):
    repo = DeviceStatisticRepository(db)
    stats = repo.get_statistics(device_id, start, end)
    if not stats:
        raise HTTPException(status_code=404, detail="Нет данных для указанного устройства")
    analysis = repo.calculate_analytics(stats)
    return analysis
