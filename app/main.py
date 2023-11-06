from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from . import models, schemas
from .database import AsyncSessionLocal
import httpx
from .schemas import WeatherDataCreate, WeatherData
from .models import WeatherData as WeatherDataModel

app = FastAPI()

# Clave API y Host para AI Weather by Meteosource
METEOSOURCE_API_KEY = '209c0a67aamsh03178906980785bp12106cjsnd81bba3eef39'
METEOSOURCE_URL = 'https://ai-weather-by-meteosource.p.rapidapi.com'

# Dependency
async def get_db():
    async with AsyncSessionLocal() as session:
        yield session

@app.get("/api/weather")
async def get_weather(latitude: float, longitude: float, timezone: str = "auto", language: str = "en", units: str = "auto", db: AsyncSession = Depends(get_db)):
    headers = {
        'X-RapidAPI-Key': METEOSOURCE_API_KEY,
        'X-RapidAPI-Host': "ai-weather-by-meteosource.p.rapidapi.com"
    }
    params = {
        "lat": latitude,
        "lon": longitude,
        "timezone": timezone,
        "language": language,
        "units": units
    }
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(f"{METEOSOURCE_URL}/current", headers=headers, params=params)
            response.raise_for_status()
        except httpx.HTTPStatusError as e:
            raise HTTPException(status_code=e.response.status_code, detail=str(e))

        data = response.json()
        return data



@app.post("/api/data", response_model=WeatherData)
async def post_data(weather_data: WeatherDataCreate, db: AsyncSession = Depends(get_db)):
    db_weather_data = WeatherDataModel(**weather_data.dict())
    db.add(db_weather_data)
    await db.commit()
    await db.refresh(db_weather_data)
    return db_weather_data

@app.get("/api/data/{data_id}", response_model=schemas.Data)
async def get_data_by_id(data_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(models.Data.query.where(models.Data.id == data_id))
    db_data = result.scalars().first()
    if db_data is None:
        raise HTTPException(status_code=404, detail="Data not found")
    return db_data
