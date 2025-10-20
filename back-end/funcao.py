from conexao import conectar

def criar_tabela():
    conexao, cursor = conectar()
    if conexao:
        try:
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS produtos (
                id SERIAL PRIMARY KEY,
                nome VARCHAR(100) NOT NULL,
                categoria VARCHAR(50),
                preco DECIMAL(10,2),
                quantidade INT
                )
            """)
            conexao.commit()
        except Exception as erro:
            print(f"erro ao criar a tabela {erro}")
        finally:
            cursor.close()
            conexao.close()
criar_tabela()

def add_produtos(nome, categoria, preco, quantidade):
    conexao, cursor = conectar()
    if conexao:
        try:
            cursor.execute(
                "INSERT INTO produtos (nome, categoria, preco, quantidade) VALUES (%s, %s, %s, %s)",
                (nome, categoria, preco, quantidade)
            )
            conexao.commit()
        except Exception as erro:
            print(f"erro ao adicionar produto {erro}")
        finally:
            cursor.close()
            conexao.close()

def atualizar_preco_quantidade(id_produtos, novo_preco, nova_quantidade):
    conexao, cursor = conectar()
    if conexao:
        try:
            cursor.execute(
                "UPDATE produtos SET preco = %s, quantidade = %s WHERE id = %s",
                (novo_preco, nova_quantidade, id_produtos)
            )
            conexao.commit()
        except Exception as erro:
            print(f"erro ao tentar atualizar preço e quantidade")
        finally:
            cursor.close()
            conexao.close()

def deletar_produto(id_produto):
    conexao, cursor = conectar()
    if conexao:
        try:
            cursor.execute(
                "DELETE FROM produtos WHERE id = %s", (id_produto,)
            )
            conexao.commit()
        except Exception as erro:
            print(f"erro ao tentar deletar produto")
        finally:
            cursor.close()
            conexao.close()



