import streamlit as st
from streamlit_drawable_canvas import st_canvas

st.set_page_config(page_title="Canvas de Dibujo", layout="centered")

st.title("🖌️ Tablero de Dibujo con Streamlit")

st.markdown("Dibuja con el mouse en el lienzo:")

# Opciones básicas
stroke_width = st.slider("Grosor del pincel:", 1, 25, 5)
stroke_color = st.color_picker("Color del pincel:", "#000000")
bg_color = st.color_picker("Color de fondo:", "#FFFFFF")

drawing_mode = st.selectbox(
    "Modo de dibujo:",
    ("freedraw", "line", "rect", "circle")
)


canvas_result = st_canvas(
    fill_color="rgba(255, 165, 0, 0.3)",
    stroke_width=stroke_width,
    stroke_color=stroke_color,
    background_color=bg_color,
    update_streamlit=True,
    height=500,
    width=500,
    drawing_mode=drawing_mode,
    key="canvas",
)

if canvas_result.json_data is not None:
    st.subheader("Datos del dibujo (JSON):")
    st.json(canvas_result.json_data)


if st.button("🧹 Limpiar lienzo"):
    st.session_state["canvas"] = None
    st.experimental_rerun()
