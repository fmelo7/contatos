# routes.py
from fastapi import APIRouter, HTTPException
from models import Contato
from database import collection
from bson import ObjectId

router = APIRouter()

@router.post("/contatos")
def criar_contato(contato: Contato):
    result = collection.insert_one(contato.dict())
    return {"id": str(result.inserted_id)}

@router.get("/contatos")
def listar_contatos():
    contatos = list(collection.find())
    for c in contatos:
        c["id"] = str(c["_id"])
        del c["_id"]
    return contatos

@router.get("/contatos/{id}")
def buscar_contato(id: str):
    contato = collection.find_one({"_id": ObjectId(id)})
    if not contato:
        raise HTTPException(status_code=404, detail="Contato não encontrado")
    contato["id"] = str(contato["_id"])
    del contato["_id"]
    return contato
