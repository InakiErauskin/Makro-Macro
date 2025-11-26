import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# 1. Título y Configuración
st.title("📊 Simulador del Modelo Renta-Gasto")
st.markdown("Ajusta las variables macroeconómicas para ver el nuevo equilibrio.")

# 2. Barra lateral para los inputs (Variables Exógenas)
st.sidebar.header("Variables Exógenas")
C0 = st.sidebar.number_input("Consumo Autónomo (C0)", value=100)
I = st.sidebar.number_input("Inversión (I)", value=50)
G = st.sidebar.number_input("Gasto Público (G)", value=50)

st.sidebar.header("Parámetros")
c = st.sidebar.slider("Propensión Marginal a Consumir (c)", 0.0, 0.99, 0.8)
t = st.sidebar.slider("Tasa Impositiva (t)", 0.0, 0.5, 0.1)

# 3. Cálculos del Modelo
# Gasto Autónomo (A)
A = C0 + I + G
# Multiplicador (k)
k = 1 / (1 - c * (1 - t))
# Renta de Equilibrio (Y*)
Y_star = k * A

# 4. Mostrar Resultados Numéricos
col1, col2 = st.columns(2)
col1.metric("Renta de Equilibrio (Y*)", f"{Y_star:.2f}")
col2.metric("Multiplicador Keynesiano", f"{k:.2f}")

# 5. Gráfico de la Cruz Keynesiana
fig, ax = plt.subplots()

# Eje X (Renta)
Y_vals = np.linspace(0, Y_star * 2, 100)
# Demanda Agregada: DA = A + c(1-t)Y
DA_vals = A + (c * (1 - t)) * Y_vals
# Recta de 45 grados (Oferta Agregada = Demanda Agregada)
ax.plot(Y_vals, Y_vals, 'k--', label='Y = DA (45°)', alpha=0.6)
# Curva de Demanda Agregada
ax.plot(Y_vals, DA_vals, 'b-', label='Demanda Agregada', linewidth=2)

# Punto de equilibrio visual
ax.plot(Y_star, Y_star, 'ro') 
ax.vlines(Y_star, 0, Y_star, linestyles='dotted', colors='r')

ax.set_title("Cruz Keynesiana")
ax.set_xlabel("Renta / Producción (Y)")
ax.set_ylabel("Demanda Agregada (DA)")
ax.legend()
ax.grid(True, alpha=0.3)

st.pyplot(fig)
