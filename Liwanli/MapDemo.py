
import streamlit as st
import pandas as pd
import numpy as np

st.header('Binhai New Area')
df = pd.DataFrame(
    np.random.randn(10, 2) / [50, 50] + [39.00, 117.75],
    columns=['lat', 'lon'])

st.map(df)