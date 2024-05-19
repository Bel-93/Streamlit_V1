import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Título de la aplicación
st.title('App de Ejemplo para Google Colab')

# Dataframe de ejemplo
df = pd.DataFrame({
    'x': np.random.randn(100),
    'y': np.random.randn(100)
    })

# Gráfico de dispersión
st.write("Gráfico de Dispersión:")
st.write(df)
st.write(plt.scatter(df['x'], df['y']))
    
