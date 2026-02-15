from sqlalchemy import Column, Integer, String
from database import Base

class FilmeDB(Base):
    __tablename__ = "filme"

    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String)
    genero = Column(String)
    nota = Column(Integer)
    classificacao = Column(Integer)
    onde_assistir = Column(String)