from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from . import models, schemas
from .database import AsyncSessionLocal
import httpx

app = FastAPI()

# Deberías inicializar la base de datos de manera asíncrona en otro lugar
# como en un evento de inicio de FastAPI
# models.Base.metadata.create_all(bind=engine)

DARKSKY_API_KEY = '209c0a67aamsh03178906980785bp12106cjsnd81bba3eef39'
DARKSKY_URL = 'https://dark-sky.p.rapidapi.com'

# Dependency
async def get_db():
    async with AsyncSessionLocal() as session:
        yield session

@app.get("/api/data")
async def get_data(latitude: float, longitude: float, db: AsyncSession = Depends(get_db)):
    headers = {
        'X-RapidAPI-Key': DARKSKY_API_KEY,
        'X-RapidAPI-Host': "dark-sky.p.rapidapi.com"
    }
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(f"{DARKSKY_URL}/{latitude},{longitude}", headers=headers, params={"units": "auto", "lang": "en"})
            response.raise_for_status()
        except httpx.HTTPStatusError as e:
            raise HTTPException(status_code=e.response.status_code, detail=str(e))

        data = response.json()
        return data

@app.post("/api/data", response_model=schemas.Data)
async def post_data(data: schemas.DataCreate, db: AsyncSession = Depends(get_db)):
    db_data = models.Data(content=data.content)
    db.add(db_data)
    await db.commit()
    await db.refresh(db_data)
    return db_data

@app.get("/api/data/{data_id}", response_model=schemas.Data)
async def get_data_by_id(data_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(models.Data.query.where(models.Data.id == data_id))
    db_data = result.scalars().first()
    if db_data is None:
        raise HTTPException(status_code=404, detail="Data not found")
    return db_data
