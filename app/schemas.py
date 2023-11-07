from pydantic import BaseModel
from typing import Optional
import datetime

class WeatherDataCreate(BaseModel):
    latitude: float
    longitude: float
    temperature: float
    wind_speed: float


class WeatherData(WeatherDataCreate):
    id: int
    recorded_at: Optional[datetime.datetime] = None

    class Config:
        orm_mode = True
