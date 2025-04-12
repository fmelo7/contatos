# models.py
from pydantic import BaseModel, EmailStr
from typing import Optional

class Contato(BaseModel):
    nome: str
    email: EmailStr
    telefone: Optional[str] = None
