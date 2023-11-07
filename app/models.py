from sqlalchemy import Column, Integer, String, Float, DateTime
from .database import Base
import datetime

# Modelo ORM de datos de clima para representar la tabla en la base de datos.
class WeatherData(Base):
    __tablename__ = "weather_data" # Nombre de la tabla en la base de datos.

    id = Column(Integer, primary_key=True, index=True)  # Clave primaria, índice para búsquedas eficientes.
    latitude = Column(Float)
    longitude = Column(Float)
    temperature = Column(Float)
    wind_speed = Column(Float)
    recorded_at = Column(DateTime, default=datetime.datetime.utcnow)


