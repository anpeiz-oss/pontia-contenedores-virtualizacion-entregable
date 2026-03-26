from config import DATABASE_URL
from contextlib import contextmanager
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# --- DB setup ---
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
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
