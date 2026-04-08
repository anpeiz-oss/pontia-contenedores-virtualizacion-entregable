from config import DATABASE_URL
from contextlib import contextmanager
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import logging

# --- Logging ---
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


# --- DB setup ---
logger.info(f"This is the resolved DATABASE_URL: {DATABASE_URL} to create the engine from.")
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False, expire_on_commit=False)
# El atributo expire_on_commit=False es necesario para que la sesión no expire al hacer commit, 
# lo que permitiría acceder a los objetos después de hacer commit.

@contextmanager
def get_session():
    """Context manager that provides a transactional session.
    Commits on success, rolls back on exception, always closes."""
    session = SessionLocal()
    try:
        yield session
        session.commit()
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()
