import streamlit  as st
import pandas as pd

dataset = pd.read_csv("CSC HOSTEL ATTENDENCE FEB-2024.csv")

st.dataframe(dataset)