import streamlit as st
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle, Polygon, Ellipse

st.title("🎅 Interaktywny Mikołaj – Streamlit")

# --- PANEL STEROWANIA ---
st.sidebar.header("⚙️ Ustawienia Mikołaja")

# Kolor stroju
suit_color = st.sidebar.color_picker("Kolor stroju Mikołaja", "#FF0000")

# Czy pokazać prezenty?
show_gifts = st.sidebar.checkbox("🎁 Pokaż prezenty", value=True)

# Grubość brody
beard_scale = st.sidebar.slider("Grubość brody", 0.5, 1.5, 1.0)

# --- RYSOWANIE ---
fig, ax = plt.subplots(figsize=(6, 8))
ax.set_aspect("equal")
ax.axis("off")

# KORPUS
body = Rectangle((-1.2, -1.0), 2.4, 2.2, color=suit_color)
ax.add_patch(body)

collar = Rectangle((-1.2, 1.0), 2.4, 0.2, color="white")
ax.add_patch(collar)

belt = Rectangle((-1.2, 0.0), 2.4, 0.2, color="black")
ax.add_patch(belt)

buckle = Rectangle((-0.3, 0.02), 0.6, 0.16, edgecolor="yellow", facecolor="none", linewidth=2)
ax.add_patch(buckle)

for y in [0.7, 0.4, 0.1]:
    ax.add_patch(Circle((0, y), 0.05, color="black"))

# NOGI I BUTY
ax.add_patch(Rectangle((-0.7, -1.5), 0.6, 0.5, color=suit_color))
ax.add_patch(Rectangle((0.1, -1.5), 0.6, 0.5, color=suit_color))
ax.add_patch(Rectangle((-0.8, -1.8), 0.8, 0.3, color="black"))
ax.add_patch(Rectangle((0.0, -1.8), 0.8, 0.3, color="black"))

# RĘCE I RĘKAWICZKI
ax.add_patch(Rectangle((-1.8, 0.5), 0.6, 1.0, angle=10, color=suit_color))
ax.add_patch(Rectangle((1.2, 0.5), 0.6, 1.0, angle=-10, color=suit_color))
ax.add_patch(Circle((-1.8, 0.5), 0.25, color="brown"))
ax.add_patch(Circle((1.8, 0.5), 0.25, color="brown"))

# GŁOWA
ax.add_patch(Circle((0, 1.6), 0.6, color="#ffddb3"))

# BRODA – sterowana suwakiem
ax.add_patch(Ellipse((0, 1.3), 1.0 * beard_scale, 0.9 * beard_scale, color="white"))
ax.add_patch(Ellipse((-0.15, 1.45), 0.5 * beard_scale, 0.2 * beard_scale, angle=15, color="white"))
ax.add_patch(Ellipse((0.15, 1.45), 0.5 * beard_scale, 0.2 * beard_scale, angle=-15, color="white"))

# NOS I OCZY
ax.add_patch(Circle((0, 1.5), 0.08, color="#e0a070"))
ax.add_patch(Circle((-0.2, 1.7), 0.06, color="white"))
ax.add_patch(Circle((0.2, 1.7), 0.06, color="white"))
ax.add_patch(Circle((-0.2, 1.7), 0.03, color="black"))
ax.add_patch(Circle((0.2, 1.7), 0.03, color="black"))
ax.plot([-0.2, 0, 0.2], [1.32, 1.28, 1.32], color="black", linewidth=2)

# CZAPKA
ax.add_patch(Polygon([(-0.8, 1.9), (0.8, 1.9), (0, 2.6)], closed=True, color=suit_color))
ax.add_patch(Rectangle((-0.8, 1.8), 1.6, 0.15, color="white"))
ax.add_patch(Circle((0, 2.65), 0.15, color="white"))

# PREZENTY – tylko jeśli checkbox zaznaczony
if show_gifts:
    ax.add_patch(Rectangle((1.6, -0.6), 0.6, 0.6, color="green"))
    ax.add_patch(Rectangle((1.86, -0.6), 0.08, 0.6, color="yellow"))
    ax.add_patch(Rectangle((1.6, -0.32), 0.6, 0.08, color="yellow"))

ax.set_xlim(-2.2, 2.4)
ax.set_ylim(-2.0, 3.0)

# WYŚWIETLANIE W STREAMLIT
st.pyplot(fig)
