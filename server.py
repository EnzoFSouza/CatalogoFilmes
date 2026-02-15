from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from pydantic import BaseModel
from typing import Optional
from fastapi.middleware.cors import CORSMiddleware
import models
import database

#Schema base para criação (POST / PUT)
class FilmeSchema(BaseModel):
    titulo: str
    genero: str
    nota: int
    classificacao: str
    onde_assistir: str

    #Permite que pydantic leia dados que vem do SQLAlchemy
    class Config:
        from_attributes = True

#Schema para atualização parcial (PATCH)
class FilmeUpdate(BaseModel):
    titulo: Optional[str] = None
    genero: Optional[str] = None
    nota: Optional[int] = None
    classificacao: Optional[str] = None
    onde_assistir: Optional[str] = None

#Cria as tabelas no banco de dados
models.Base.metadata.create_all(bind=database.engine)

#Inicializando a aplicacao
app = FastAPI()

# Configuração do CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5500",
        "http://127.0.0.1:5500"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#GET --> Listar e Consultar
@app.get("/filmes")
def listar_filmes(db: Session = Depends(database.get_db)):
    return db.query(models.FilmeDB).all()

@app.get("/filmes/{id_filme}")
def consultar_filme(id_filme: int, db: Session = Depends(database.get_db)):
    #No SQLAlchemy, utilizar .query para buscar no banco
    filme = db.query(models.FilmeDB).filter(models.FilmeDB.id == id_filme).first()
    
    if not filme:
        raise HTTPException(status_code=404, detail="Filme não encontrado")
    return filme

#POST --> Criar
@app.post("/filmes", status_code=status.HTTP_201_CREATED)
def criar_filme(filme: FilmeSchema, db: Session = Depends(database.get_db)):
    #Cria uma instância do modelo do banco com os dados do Pydantic
    novo_filme = models.FilmeDB(**filme.model_dump())

    db.add(novo_filme) #Adiciona
    db.commit() #Salva
    db.refresh(novo_filme) #Atualiza o objeto com o ID gerado pelo banco
    return novo_filme

#PUT --> Update total
@app.put("/filmes/{id_filme}")
def atualizar_filme_total(id_filme: int, filme_data: FilmeSchema, db: Session = Depends(database.get_db)):
    filme_query = db.query(models.FilmeDB).filter(models.FilmeDB.id == id_filme)
    filme = filme_query.first()

    if not filme:
        raise HTTPException(status_code=404, detail="Filme não encontrado")
    
    #O .update() do SQLAlchemy substitui os campos
    filme_query.update(filme_data.model_dump())
    db.commit()
    return filme_query.first()

#PATCH --> Update parcial
@app.patch("/filmes/{id_filme}")
def atualizar_filme_parcial(id_filme: int, filme_data: FilmeUpdate, db: Session = Depends(database.get_db)):
    filme_query = db.query(models.FilmeDB).filter(models.FilmeDB.id == id_filme)
    filme = filme_query.first()

    if not filme:
        raise HTTPException(status_code=404, detail="Filme não encontrado")
    
    dados_atualizar = filme_data.model_dump(exclude_unset=True)
    filme_query.update(dados_atualizar)
    db.commit()
    return filme_query.first()

#DELETE
@app.delete("/filmes/{id_filme}", status_code=status.HTTP_204_NO_CONTENT)
def deletar_filme(id_filme: int, db: Session = Depends(database.get_db)):
    filme_query = db.query(models.FilmeDB).filter(models.FilmeDB.id == id_filme)
    if not filme_query.first():
        raise HTTPException(status_code=404, detail="Filme não encontrado")
    
    filme_query.delete()
    db.commit()
    return None #204 pede corpo vazio