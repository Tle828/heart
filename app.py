import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="Heart", page_icon="❤️")

st.title("❤️ I miss you ❤️")

t = np.linspace(0, 2*np.pi, 1000)

x = 16 * np.sin(t)**3
y = (13 * np.cos(t)
     - 5 * np.cos(2*t)
     - 2 * np.cos(3*t)
     - np.cos(4*t))

fig, ax = plt.subplots()
ax.fill(x, y, color='red')
ax.set_facecolor('black')
fig.patch.set_facecolor('black')
ax.axis('off')

st.pyplot(fig)