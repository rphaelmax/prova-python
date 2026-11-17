import pandas as pd
import streamlit as st
import plotly.express as px
import openpyxl

st.set_page_config(page_title="Dados Educação", layout="wide")
st.title("Dados Educação")

df = pd.read_excel("dados-educacao.xlsx", engine="openpyxl")

df_filtrado = df[
    (df["genero"].isin(["Masculino", "Feminino"])) &
    (df["escolaridade"] == "Mestrado")
].copy()

df_tabela = df_filtrado[["genero", "escolaridade"]]

st.sidebar.header("Controles")
opcao = st.sidebar.radio("Selecione a visualização:", ["Tabela", "Graficos"])

if opcao == "Tabela":
    st.header("Tabela de gênero e escolaridade")
    st.dataframe(df_tabela, use_container_width=True, hide_index=True)

elif opcao == "Graficos":
    st.header("Gráficos de gênero e escolaridade") 

    df_masculino = df_tabela[df_tabela["genero"] == "Masculino"]

    fig_barra_masculino = px.bar(
        df_masculino,
        barmode="group",
        title="Quantidade de pessoas masculinas com mestrado concluído",
        template="plotly_dark"
    )
    fig_barra_masculino.update_xaxes(type="category")
    st.plotly_chart(fig_barra_masculino, use_container_width=True)

    df_feminino = df_tabela[df_tabela["genero"] == "Feminino"]

    fig_barra_feminino = px.bar(
        df_feminino,
        barmode="group",
        title="Quantidade de pessoas femininas com mestrado concluído",
        template="plotly_dark"
    )
    fig_barra_feminino.update_xaxes(type="category")
    st.plotly_chart(fig_barra_feminino, use_container_width=True)