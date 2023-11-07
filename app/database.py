from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# URL de conexión para la base de datos MySQL.
SQLALCHEMY_DATABASE_URL = "mysql+aiomysql://usuario:contraseña@db/pruebatecnica"


# Crea el motor de la base de datos para comunicación asíncrona.
engine = create_async_engine(
    SQLALCHEMY_DATABASE_URL
)

# Configura la sesión para ser utilizada con el ORM y la conexión asíncrona.
AsyncSessionLocal = sessionmaker(
    engine, class_=AsyncSession, expire_on_commit=False
)
# Base para declarar modelos ORM de SQLAlchemy.
Base = declarative_base()
