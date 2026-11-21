"""Configurazione backend"""

import os


def _database_url() -> str:
    url = os.getenv("DATABASE_URL", "sqlite:///./museo.db")
    # SQLAlchemy vuole il nome del driver nell'indirizzo: usiamo psycopg
    if url.startswith("postgres://"):
        url = url.replace("postgres://", "postgresql+psycopg://", 1)
    elif url.startswith("postgresql://"):
        url = url.replace("postgresql://", "postgresql+psycopg://", 1)
    return url


DEV_SECRET_KEY = "zSAOm2zxpq97xNLrlxJlSnErGFPOlZRUzgilcUjRh-E"

DATABASE_URL = _database_url()

# Chiave usata per firmare i token di accesso JWT
SECRET_KEY = os.getenv("SECRET_KEY", DEV_SECRET_KEY)

# Scadenza dei token JWT in minuti
TOKEN_EXPIRE_MINUTES = int(os.getenv("TOKEN_EXPIRE_MINUTES", "120"))

# Regola del museo: le prenotazioni si chiudono 2 giorni prima dell'attività
GIORNI_PREAVVISO = int(os.getenv("GIORNI_PREAVVISO", "2"))

# Oltre questo numero di persone si applica la tariffa di gruppo
SOGLIA_GRUPPO = 20

# Numero massimo di biglietti in una prenotazione
MAX_BIGLIETTI = 40

# Controllo per la SECRET_KEY
if not DATABASE_URL.startswith("sqlite") and SECRET_KEY == DEV_SECRET_KEY:
    raise RuntimeError("In produzione è obbligatorio impostare la variabile d'ambiente SECRET_KEY")