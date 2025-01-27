import streamlit as st
import pandas as pd
import numpy as np

chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])

st.area_chart(chart_data)

titanic = pd.read_csv("titanic.csv")

st.title("Titanic, Supervivientes:")

st.table(data=titanic[["Cabin", "Ticket"]])

st.write("Edad promedio de los pasajeros: ", titanic["Age"].mean())

st.line_chart(data=titanic["Age"])
