import streamlit as st
import requests

#url
API_URL = "http://127.0.0.1:8000"

#python -m streamlit run app.py

st.set_page_config(page_title="Controle de produtos e estoque", page_icon="📦")
st.title("Controle de produtos e estoque")

menu = st.sidebar.radio("navegação", ["listar produtos", "adicionar produtos", "atualizar preço/quantidade", "deletar produto"])

if menu == "listar produtos":
    st.subheader("todos os produtos disponiveis")
    response = requests.get(f"{API_URL}/produtos")
    if response.status_code == 200:
        produtos = response.json().get("produtos", [])
        if produtos:
            st.dataframe(produtos)
    else:
        st.error("erro ao acessar a API")

elif menu == "adicionar produtos":
    st.subheader("adicionar produtos")
    nome = st.text_input("nome do produto")
    categoria = st.text_input("categoria pertencente")
    preco = st.number_input("digite o preço", min_value=0.0, format="%.2f")
    quantidade = st.number_input("digite a quantidade disponível")
    if st.button("adicionar"):
        dados = {"nome": nome, "categoria": categoria, "preco": preco, "quantidade": quantidade}
        response = requests.post(f"{API_URL}/produtos", params=dados)
        if response.status_code == 200:
            st.success("produto adicionado com sucesso")
        else:
            st.error("erro ao adicionar o produto")

elif menu == "atualizar preço/quantidade":
    st.subheader("atualizar")
    id_produtos = st.number_input("digite o id do produto", min_value=1, step=1)
    preco = st.number_input("digite o novo preço", min_value=0.0, format="%.2f")
    quantidade = st.number_input("digite a nova quantidade", min_value=1, step=1)
    if st.button("atualizar"):
        dados = {"preco": preco, "quantidade": quantidade}
        response = requests.put(f"{API_URL}/produtos/{id_produtos}", params=dados)
        if response.status_code == 200:
            st.success("produto atualizado com sucesso")
        else:
            st.error("erro ao atualizar o produto")

