import streamlit as st
import requests

# --- CONFIGURACIÓN DE LA PÁGINA MÓVIL ---
st.set_page_config(page_title="Panel CEO", page_icon="🚀", layout="centered")

# --- TU ENLACE SECRETO DE MAKE ---
# Reemplaza esto con tu Webhook real de Make, conservando las comillas
MAKE_WEBHOOK_URL = "https://hook.us2.make.com/7gwzs8q25amgf72xlpwatafvhgfvgal3"

# --- DISEÑO DEL PANEL ---
st.title("📱 Centro de Mando CEO")
st.write("Selecciona un nicho. La IA buscará el producto más viral, redactará el anuncio y lo publicará automáticamente.")
st.divider()

st.subheader("🎯 Categorías Virales")

# --- FUNCIÓN DE LANZAMIENTO A LA NUBE ---
def lanzar_campana(categoria):
    # Ahora solo le enviamos el "Tema" a Make. Make hará el resto.
    datos_para_ia = {"categoria": categoria}
    try:
        respuesta = requests.post(MAKE_WEBHOOK_URL, json=datos_para_ia)
        if respuesta.status_code == 200:
            st.success(f"¡Orden ejecutada! Make está buscando un producto único de '{categoria}' y creando la campaña.")
        else:
            st.warning("La orden se envió, pero revisa tu escenario en Make.")
    except Exception as e:
        st.error(f"Error de conexión con Make: {e}")

# --- BOTONES ESTRATÉGICOS DEL CEO ---
if st.button("💻 Búsqueda Viral: Tecnología", use_container_width=True):
    lanzar_campana("Tecnología")

if st.button("🐶 Búsqueda Viral: Mascotas", use_container_width=True):
    lanzar_campana("Mascotas")

if st.button("🛋️ Búsqueda Viral: Hogar y Estética", use_container_width=True):
    lanzar_campana("Hogar y Estética")

if st.button("🧘‍♀️ Búsqueda Viral: Salud y Bienestar", use_container_width=True):
    lanzar_campana("Salud y Bienestar")

st.divider()
st.caption("Sistema Operativo IA - Ejecución en la Nube ☁️")
