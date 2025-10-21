import streamlit as st
import requests

#url
# "http://127.0.0.1:8000"

#python -m streamlit run app.py

st.set_page_config(page_title="Controle de produtos e estoque"), page_icon="📦"
st.title("Controle de produtos e estoque")

menu = st.sidebar.radio("navegação", ["adiconar produtos", "listar produtos", "atualizar preço/quantidade", "deletar produto"])

