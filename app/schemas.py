from pydantic import BaseModel
from datetime import datetime

class DeviceStatisticCreate(BaseModel):
    device_id: str
    timestamp: datetime
    x: float
    y: float
    z: float

    class Config:
        orm_mode = True

class AxisAnalysis(BaseModel):
    min: float
    max: float
    count: int
    sum: float
    median: float

class AnalysisResponse(BaseModel):
    x: AxisAnalysis
    y: AxisAnalysis
    z: AxisAnalysis
