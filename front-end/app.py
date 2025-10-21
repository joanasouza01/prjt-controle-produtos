import streamlit as st
import requests

#url
API_URL = "http://127.0.0.1:8000"

#python -m streamlit run app.py

st.set_page_config(page_title="Controle de produtos e estoque", page_icon="📦")
st.title("Controle de produtos e estoque")

menu = st.sidebar.radio("navegação", ["listar produtos", "adiconar produtos", "atualizar preço/quantidade", "deletar produto"])

if menu == "listar":
    st.subheader("todos os produtos disponiveis")
    response = requests.get(f"{API_URL}/produtos")
    if response.status_code == 200:
        produtos = response.json().get("produtos", [])
        if produtos:
            st.dataframe(produtos)
    else:
        st.error("erro ao acessar a API")
