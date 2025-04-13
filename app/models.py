from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from app.database import Base
from datetime import datetime


class DeviceStatistic(Base):
    __tablename__ = "device_statistics"

    id = Column(Integer, primary_key=True, index=True)
    device_id = Column(String, index=True, nullable=False)
    timestamp = Column(DateTime, default=datetime.utcnow, index=True)
    x = Column(Float, nullable=False)
    y = Column(Float, nullable=False)
    z = Column(Float, nullable=False)

# Опционально: модели для пользователей и устройств
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)

class Device(Base):
    __tablename__ = "devices"

    id = Column(String, primary_key=True, index=True)  # device_id как строка
    user_id = Column(Integer, ForeignKey("users.id"), nullable=True)
