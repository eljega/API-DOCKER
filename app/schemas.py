from pydantic import BaseModel
from typing import Optional
import datetime

# Schema para la creacion de datos de clima, usado para validar datos entrantes.
class WeatherDataCreate(BaseModel):
    latitude: float
    longitude: float
    temperature: float
    wind_speed: float

# Schema para la representacion de datos de clima, incluye el ID y la marca de tiempo.
class WeatherData(WeatherDataCreate):
    id: int
    recorded_at: Optional[datetime.datetime] = None

    class Config:
        orm_mode = True # Permite la compatibilidad con ORMs, como SQLAlchemy.
