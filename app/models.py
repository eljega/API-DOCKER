from sqlalchemy import Column, Integer, String, Float, DateTime
from .database import Base
import datetime

class WeatherData(Base):
    __tablename__ = "weather_data"

    id = Column(Integer, primary_key=True, index=True)
    latitude = Column(Float)
    longitude = Column(Float)
    temperature = Column(Float)
    wind_speed = Column(Float)
    recorded_at = Column(DateTime, default=datetime.datetime.utcnow)


