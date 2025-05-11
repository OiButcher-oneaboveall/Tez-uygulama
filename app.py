
import streamlit as st
from optimizer import get_best_route

st.title("🚀 Tez Uygulaması")

if st.button("Rota Hesapla"):
    rota, süre, yakıt, emisyon, risk, log = get_best_route()
    st.success(f"En iyi rota: {rota}")
    st.info(f"Süre: {süre} dk, Yakıt: {yakıt} L, Emisyon: {emisyon} kg, Risk: {risk}")
