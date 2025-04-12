# main.py
from fastapi import FastAPI
from routes import router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Cadastro de Contatos")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # ou substitua por ["http://localhost:port"] se quiser mais segurança
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Importando o roteador do arquivo routes.py
app.include_router(router)
