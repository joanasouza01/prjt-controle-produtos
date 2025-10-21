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

@app.get("/produtos")
def listar_produtos():
    produtos = funcao.listar_produtos()
    lista = []
    for linha in produtos:
        lista.append({"id": linha[0],
                      "nome": linha[1],
                      "categoria": linha[2],
                      "preco": linha[3],
                      "quantidade": linha[4]
                    })
    return{"produtos": lista}

@app.put("/produtos/{id_produtos}")
def atualizar__preco_quantidade(id_produtos: int, novo_preco: float, nova_quantidade: int):
    produto = funcao.atualizar_preco_quantidade(id_produtos)
    if produto:
        funcao.atualizar_preco_quantidade(id_produtos, novo_preco, nova_quantidade)
        return{"mensagem": "produto atualizado com sucesso"}
    else:
        return{"erro": "produto não encontrado"}