"""Configurazione del database"""

from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

from . import config


class Base(DeclarativeBase):
    """Classe base dei modelli: ogni classe che eredita da Base diventa una tabella."""


connect_args = {}
if config.DATABASE_URL.startswith("sqlite"):
    # Con SQLite va disattivato un controllo, perché FastAPI usa le connessioni da thread diversi.
    connect_args = {"check_same_thread": False}

engine = create_engine(config.DATABASE_URL, connect_args=connect_args, pool_pre_ping=True)

# expire_on_commit=False: dopo il commit gli oggetti restano leggibili senza rileggerli dal database.
SessionLocal = sessionmaker(bind=engine, expire_on_commit=False)


def get_db():
    """Apre una sessione per ogni richiesta e la chiude automaticamente alla fine."""
    with SessionLocal() as db:
        yield db