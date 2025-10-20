from fastapi import FastAPI
import funcao

#python -m uvicorn api:app --reload

#testar api FastAPI
app = FastAPI(title="Gerenciador de produtos")
#/docs > documentação swagger
#/redoc > documentação redoc

#GET = pegar / listar
#POST = criar / enviar
#PUT = atualizar 
#DELETE = deletar


@app.get("/")
def home():
    return{"mensagem": "produtos"}

@app.post("/produtos")
def colocar_produtos(nome: str, categoria: str, preco: float, quantidade: int):
    funcao.add_produtos(nome, categoria, preco, quantidade)
    return{"mensagem": "produto adicionado com sucesso!"}

@app.