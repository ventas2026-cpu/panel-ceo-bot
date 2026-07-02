import streamlit as st
import requests

# --- CONFIGURACIÓN DE LA PÁGINA MÓVIL ---
st.set_page_config(page_title="Panel CEO", page_icon="📱", layout="centered")

# Reemplaza este enlace con tu Webhook real de Make
MAKE_WEBHOOK_URL = "https://hook.us1.make.com/tu_codigo_secreto" 

st.title("🚀 Centro de Mando CEO")
st.write("Conexión API: CJ Dropshipping & AliExpress (En desarrollo)")
st.divider()

# Simulador de la API (Próximamente inyectaremos los datos reales aquí)
productos_api = [
    {"nombre": "Cama Nube Mascotas", "costo_fabrica": 20.00, "envio": 2.50, "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3a/Cat03.jpg/800px-Cat03.jpg"},
    {"nombre": "Humidificador Llama", "costo_fabrica": 15.00, "envio": 4.00, "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/87/A_simple_humidifier.jpg/800px-A_simple_humidifier.jpg"},
    {"nombre": "Corrector Postura", "costo_fabrica": 10.00, "envio": 0.00, "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/75/Posture_correction.jpg/800px-Posture_correction.jpg"}
]

# --- EL NUEVO ALGORITMO DEL 15% DE GANANCIA ---
for prod in productos_api:
    if prod["envio"] <= 5.00:
        costo_total = prod["costo_fabrica"] + prod["envio"]
        # Nuevo margen estratégico del 15% establecido por el CEO
        precio_venta_15 = costo_total * 1.15 
        
        col1, col2 = st.columns([1, 2])
        
        with col1:
            st.image(prod["img"], use_column_width=True)
            
        with col2:
            st.subheader(prod["nombre"])
            st.write(f"Costo Fábrica: ${prod['costo_fabrica']:.2f}")
            st.write(f"Envío Express: ${prod['envio']:.2f}")
            
            # Botón interactivo con el nuevo margen
            if st.button(f"Lanzar a ${precio_venta_15:.2f} (15% Margen)", key=f"15_{prod['nombre']}"):
                datos_para_ia = {
                    "producto": prod["nombre"], 
                    "precio": f"${precio_venta_15:.2f}",
                    "imagen_url": prod["img"]
                }
                
                try:
                    requests.post(MAKE_WEBHOOK_URL, json=datos_para_ia)
                    st.success(f"¡Orden enviada! La IA está creando la publicidad.")
                except Exception as e:
                    st.error(f"Fallo en la conexión: {e}")
                    
        st.divider()
