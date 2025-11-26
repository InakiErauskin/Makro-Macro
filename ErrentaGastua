import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# --- KONFIGURAZIOA ---
st.set_page_config(page_title="Errenta-Gastu Eredua", layout="wide")

st.title("📈 Simulagailu Makroekonomikoa: Errenta-Gastu Eredua")
st.markdown("""
Eredu interaktibo honek ondasun-merkatuko oreka simulatzen du (Gurutze Keynesiarra).
Oreka-baldintza honako hau da: **Produkzioa (Y) = Eskari Agregatua (DA)**.
""")

# --- ALBOKO BARRA (ERABILTZAILEAREN DATUAK) ---
st.sidebar.header("1. Aldagai Exogenoak")
st.sidebar.markdown("Osagai autonomoak zehaztu:")
C0 = st.sidebar.number_input("Kontsumo Autonomoa (C0)", value=100.0, step=10.0)
I0 = st.sidebar.number_input("Inbertsio Autonomoa (I0)", value=80.0, step=10.0)
G0 = st.sidebar.number_input("Gastu Publikoa (G0)", value=150.0, step=10.0)

st.sidebar.header("2. Parametroak")
c = st.sidebar.slider("Kontsumitzeko Joera Marjinala (c)", 0.1, 0.95, 0.8)
t = st.sidebar.slider("Zerga-tasa (t)", 0.0, 0.5, 0.2)

# --- KALKULU MAKROEKONOMIKOAK ---

# 1. Gastu Autonomo Osoa (A)
A = C0 + I0 + G0

# 2. Biderkatzaile Keynesiarra (k)
denominador = 1 - c * (1 - t)
multiplicador = 1 / denominador

# 3. Oreka-Errenta (Y*)
Y_star = multiplicador * A

# --- DATUEN BISTARATZEA ---

# Emaitza numerikoak
col1, col2, col3 = st.columns(3)
col1.metric("Gastu Autonomoa (A)", f"{A:.2f}")
col2.metric("Biderkatzailea (k)", f"{multiplicador:.2f}")
col3.metric("Oreka-Errenta (Y*)", f"{Y_star:.2f}", delta_color="normal")

# --- GRAFIKOA (MATPLOTLIB) ---
st.subheader("Gurutze Keynesiarraren Grafikoa")

# Datuak sortu
Y_max = Y_star * 2 if Y_star > 0 else 100
Y_values = np.linspace(0, Y_max, 100)

# Eskari Agregatuaren ekuazioa: DA = A + (c*(1-t)) * Y
pendiente_DA = c * (1 - t)
DA_values = A + (pendiente_DA * Y_values)

# Irudia sortu
fig, ax = plt.subplots(figsize=(10, 6))

# 1. 45 graduko lerroa (Eskaintza = Eskaria)
ax.plot(Y_values, Y_values, color='black', linestyle='--', alpha=0.5, label='Y = DA (45°)')

# 2. Eskari Agregatuaren lerroa
ax.plot(Y_values, DA_values, color='blue', linewidth=2.5, label='Eskari Agregatua (DA)')

# 3. Oreka-puntua
ax.scatter([Y_star], [Y_star], color='red', s=100, zorder=5, label='Oreka')
# Lerroak ardatzetara
ax.vlines(Y_star, 0, Y_star, color='red', linestyle=':', alpha=0.6)
ax.hlines(Y_star, 0, Y_star, color='red', linestyle=':', alpha=0.6)

# Etiketak eta Estiloa
ax.set_xlabel("Errenta / Produkzioa (Y)")
ax.set_ylabel("Eskari Agregatua (DA)")
ax.set_title(f"Oreka Biderkatzailea = {multiplicador:.2f} denean")
ax.legend()
ax.grid(True, alpha=0.3)
ax.set_xlim(0, Y_max)
ax.set_ylim(0, Y_max)

# Grafikoa Streamlit-en erakutsi
st.pyplot(fig)

# --- AZALPENA ---
st.info(f"""
**Analisia:** Gastu Autonomoa **{A}** eta biderkatzailea **{multiplicador:.2f}** direnean, 
ekonomia **{Y_star:.2f}** produkzio-mailan orekatzen da.
Gastu Publikoa (G0) unitate bat handitzen baduzu, Errenta (Y*) {multiplicador:.2f} unitate handituko da.
""")
