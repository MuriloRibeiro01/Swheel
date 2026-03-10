# Ponto de entrada do sistema

from fastapi import FastAPI

# Cria a "instância" FastAPI
app = FastAPI()

x = 5

# cria um path e define um método 
@app.get("/")
async def root():
    return {"number": x}

# Planos futuros: utilizar essa API para criar testes unitários
# tanto para questão de estudos, quanto para qualidade do software.