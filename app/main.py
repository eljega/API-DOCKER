from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from . import models, schemas, database
from .database import engine


models.Base.metadata.create_all(bind=engine)


app = FastAPI()

# Dependency
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/api/data")
async def get_data():
    # Aquí iría la lógica para obtener datos de una API externa
    # Por ejemplo, utilizando 'requests' o 'httpx' para hacer una llamada HTTP
    # Debes reemplazar 'external_data' con la respuesta de la API externa
    external_data = {"sample_data": "This is a test"}
    return external_data

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
