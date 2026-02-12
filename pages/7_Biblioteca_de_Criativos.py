import streamlit as st
import pandas as pd

st.title("📚 Biblioteca de Criativos")

df = pd.read_csv("data/criativos.csv")

st.sidebar.header("Filtros")

etapa = st.sidebar.multiselect(
    "Etapa do funil",
    options=df["etapa"].unique(),
    default=df["etapa"].unique()
)

uso = st.sidebar.multiselect(
    "Uso recomendado",
    options=df["uso_recomendado"].unique(),
    default=df["uso_recomendado"].unique()
)

df_filtrado = df[
    (df["etapa"].isin(etapa)) &
    (df["uso_recomendado"].isin(uso))
]

st.dataframe(df_filtrado, use_container_width=True)

st.info("📌 Use esta tabela para decidir qual criativo escalar sem contaminar o funil.")
