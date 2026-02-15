from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#Nome do arquivo do banco
SQLALCHEMY_DATABASE_URL = "sqlite:///./filmes.db"

#Engine é quem conversa com SQLite
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

#Cada instância da SessionLocal será uma sessão do banco
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

#Classe base para criar os modelos
Base = declarative_base()

#Função que abre e fecha a conexão automaticamente (Dependency Injection)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()