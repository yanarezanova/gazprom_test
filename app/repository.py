
from sqlalchemy.orm import Session
from typing import List, Optional
from datetime import datetime
from app.models import DeviceStatistic
from app.schemas import DeviceStatisticCreate
import statistics


class DeviceStatisticRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_statistic(self, stat_in: DeviceStatisticCreate) -> DeviceStatistic:
        stat = DeviceStatistic(
            device_id=stat_in.device_id,
            timestamp=stat_in.timestamp,
            x=stat_in.x,
            y=stat_in.y,
            z=stat_in.z
        )
        self.db.add(stat)
        self.db.commit()
        self.db.refresh(stat)
        return stat

    def get_statistics(
            self, device_id: str, start: Optional[datetime] = None, end: Optional[datetime] = None
    ) -> List[DeviceStatistic]:
        query = self.db.query(DeviceStatistic).filter(DeviceStatistic.device_id == device_id)
        if start:
            query = query.filter(DeviceStatistic.timestamp >= start)
        if end:
            query = query.filter(DeviceStatistic.timestamp <= end)
        return query.all()

    def calculate_analytics(self, stats: List[DeviceStatistic]):
        # Собираем списки значений для каждого из полей
        x_values = [s.x for s in stats]
        y_values = [s.y for s in stats]
        z_values = [s.z for s in stats]

        def analyze(values: list) -> dict:
            return {
                "min": min(values) if values else None,
                "max": max(values) if values else None,
                "count": len(values),
                "sum": sum(values),
                "median": statistics.median(values) if values else None
            }

        return {
            "x": analyze(x_values),
            "y": analyze(y_values),
            "z": analyze(z_values)
        }
