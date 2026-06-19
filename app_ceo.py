import streamlit as st
import requests

# --- CONFIGURACIÓN DE LA PÁGINA MÓVIL ---
st.set_page_config(page_title="Panel CEO", page_icon="📱", layout="centered")

# Enlace de Make (Simulador por ahora)
MAKE_WEBHOOK_URL = "https://hook.us2.make.com/7gwzs8q25amgf72xlpwatafvhgfvgal3"

# Simulador de los productos recomendados por la IA
productos_encontrados = [
    {"nombre": "Cama Nube Mascotas", "costo": 12.00, "envio": 2.50, "img": "https://via.placeholder.com/150/FFB6C1/000000?text=Cama"},
    {"nombre": "Humidificador Llama", "costo": 15.00, "envio": 0.00, "img": "https://via.placeholder.com/150/FFA500/000000?text=Llama"},
    {"nombre": "Corrector Postura", "costo": 8.00, "envio": 1.50, "img": "https://via.placeholder.com/150/ADD8E6/000000?text=Postura"},
    {"nombre": "Cepillo Quita Pelos", "costo": 4.00, "envio": 4.50, "img": "https://via.placeholder.com/150/90EE90/000000?text=Cepillo"},
    {"nombre": "Lámpara Galaxia", "costo": 18.00, "envio": 3.00, "img": "https://via.placeholder.com/150/9370DB/FFFFFF?text=Galaxia"}
]

# --- ENCABEZADO ---
st.title("🚀 Panel de Mando CEO")
st.write("Catálogo de Oportunidades - Selecciona el producto ganador del turno.")
st.divider()

# --- CATÁLOGO CON LÓGICA DE NEGOCIO ---
for prod in productos_encontrados:
    if prod["envio"] <= 5.00:
        costo_total = prod["costo"] + prod["envio"]
        precio_venta = costo_total * 1.20 # 20% margen de ganancia
        
        col1, col2 = st.columns([1, 2])
        
        with col1:
            st.image(prod["img"], use_column_width=True)
            
        with col2:
            st.subheader(prod["nombre"])
            st.write(f"**Costo Total (con envío):** ${costo_total:.2f}")
            st.write(f"**Precio de Venta Sugerido:** ${precio_venta:.2f}")
            
            if st.button(f"Lanzar Publicidad", key=prod['nombre']):
                datos_para_ia = {"producto": prod["nombre"], "precio": f"${precio_venta:.2f}"}
                try:
                    # requests.post(MAKE_WEBHOOK_URL, json=datos_para_ia)
                    st.success(f"¡Orden ejecutada! La IA está creando anuncios para {prod['nombre']}.")
                except Exception as e:
                    st.error(f"Fallo en la conexión: {e}")
                    
        st.divider()
