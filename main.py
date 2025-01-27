import streamlit as st
import pandas as pd
import numpy as np


titanic = pd.read_csv("titanic.csv")

st.title("Titanic, Supervivientes:")

st.write("Edad promedio de los pasajeros: ", titanic["Age"].mean())

st.metric(label="Promedio de Edad", value=titanic["Age"].mean())

st.line_chart(data=titanic["Age"])

st.dataframe(data=titanic[["Survived", "Age"]])

st.table(data=titanic[["Age", "Sex"]])

st.dataframe(data=titanic[["Survived", "Age"]])

st.area_chart(data=titanic[["Age", "Survived"]])

st.table(data=titanic[["Age", "Sex"]])

chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])

st.area_chart(chart_data)

titanic = pd.read_csv("titanic.csv")

st.title("Titanic, Supervivientes:")

st.table(data=titanic[["Cabin", "Ticket"]])

st.write("Edad promedio de los pasajeros: ", titanic["Age"].mean())

st.line_chart(data=titanic["Age"])

"""Ticket
 Objetivo: Usando https://docs.streamlit.io/develop/api-reference crear 3 elementos para mostrar datos de Titanic.
 Los datos están en Pandas ->  
    Ejemplos - ayuda: 
        https://pandas.pydata.org/docs/getting_started/intro_tutorials/03_subset_data.html
        https://pandas.pydata.org/docs/getting_started/intro_tutorials/06_calculate_statistics.html

"""

