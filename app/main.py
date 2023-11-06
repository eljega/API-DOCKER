from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from . import models, schemas, database
from .database import engine
from fastapi import FastAPI, HTTPException
import httpx



models.Base.metadata.create_all(bind=engine)

# Reemplaza 'your_api_key' con tu clave de API real de Dark Sky
DARKSKY_API_KEY = '209c0a67aamsh03178906980785bp12106cjsnd81bba3eef39'
DARKSKY_URL = 'https://dark-sky.p.rapidapi.com'


app = FastAPI()

# Dependency
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/api/data")
async def get_data(latitude: float, longitude: float):
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
async def post_data(data: schemas.DataCreate, db: Session = Depends(get_db)):
    db_data = models.Data(content=data.content)
    db.add(db_data)
    db.commit()
    db.refresh(db_data)
    return db_data

@app.get("/api/data/{data_id}", response_model=schemas.Data)
async def get_data_by_id(data_id: int, db: Session = Depends(get_db)):
    db_data = db.query(models.Data).filter(models.Data.id == data_id).first()
    if db_data is None:
        raise HTTPException(status_code=404, detail="Data not found")
    return db_data
