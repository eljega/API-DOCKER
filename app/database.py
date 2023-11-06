from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "mysql+aiomysql://eljega:12345@db/pruebatecnica"

# Crear un motor asincrónico.
engine = create_async_engine(
    SQLALCHEMY_DATABASE_URL
)

# La clase de sesión que controla las operaciones de la base de datos ahora debe ser asincrónica.
AsyncSessionLocal = sessionmaker(
    engine, class_=AsyncSession, expire_on_commit=False
)

Base = declarative_base()
