import streamlit as st
import requests

# --- CONFIGURACIÓN DE LA PÁGINA MÓVIL ---
st.set_page_config(page_title="Panel CEO", page_icon="📱", layout="centered")

# --- CONEXIONES MAESTRAS ---
MAKE_WEBHOOK_URL = "https://hook.us2.make.com/7gwzs8q25amgf72xlpwatafvhgfvgal3" # Reemplaza con tu Webhook de Make
CJ_API_KEY = "CJ5573236@api@ab9c33944d684db38640855af3afe4c1" # <--- ¡Pega tu llave de CJ Dropshipping aquí!

st.title("🚀 Centro de Mando CEO")
st.write("Catálogo en Vivo: CJ Dropshipping")
st.divider()

# --- MOTOR DE BÚSQUEDA AUTOMÁTICA ---
def obtener_productos_cj():
    # Enlace oficial de la base de datos de CJ Dropshipping
    url = "https://developers.cjdropshipping.com/api2.0/v1/product/list"
    
    # Aquí presentamos tu "identificación" oficial usando la API Key
    headers = {
        "CJ-Access-Token": CJ_API_KEY,
        "Content-Type": "application/json"
    }
    
    # Le decimos al algoritmo qué buscar (Ejemplo: 5 productos de Mascotas)
    payload = {
        "pageSize": 5,
        "categoryName": "Pet" 
    }
    
    try:
        # Python viaja a China en fracciones de segundo y trae la respuesta
        response = requests.post(url, headers=headers, json=payload)
        if response.status_code == 200:
            datos = response.json()
            return datos.get("data", {}).get("list", [])
        else:
            st.error("Error al conectar con CJ Dropshipping. Revisa tu API Key.")
            return []
    except Exception as e:
        st.error(f"Fallo en la conexión: {e}")
        return []

# Ejecutamos el motor de búsqueda
productos_reales = obtener_productos_cj()

# --- EL ALGORITMO FINANCIERO DEL CEO ---
if productos_reales:
    for prod in productos_reales:
        # Extraemos los datos reales del proveedor
        nombre = prod.get("productNameEn", "Producto sin nombre")
        precio_fabrica = float(prod.get("sellPrice", 0))
        imagen = prod.get("productImage", "")
        
        # Simulamos un costo de envío base de $4.50 para el cálculo automático
        costo_envio = 4.50 
        
        if costo_envio <= 5.00:
            costo_total = precio_fabrica + costo_envio
            
            # Aplicamos tu estrategia de margen agresivo del 15%
            precio_venta_15 = costo_total * 1.15 
            
            col1, col2 = st.columns([1, 2])
            
            with col1:
                if imagen:
                    st.image(imagen, use_column_width=True)
                
            with col2:
                # Cortamos los nombres si son excesivamente largos
                st.subheader(nombre[:60] + "...") 
                st.write(f"**Costo Fábrica:** ${precio_fabrica:.2f}")
                st.write(f"**Envío (Est.):** ${costo_envio:.2f}")
                
                if st.button(f"Lanzar a ${precio_venta_15:.2f} (15% Margen)", key=prod.get("pid")):
                    datos_para_ia = {
                        "producto": nombre, 
                        "precio": f"${precio_venta_15:.2f}",
                        "imagen_url": imagen
                    }
                    
                    try:
                        requests.post(MAKE_WEBHOOK_URL, json=datos_para_ia)
                        st.success("¡Orden enviada a Make! La IA está creando la publicidad en este instante.")
                    except Exception as e:
                        st.error(f"Fallo en el Webhook: {e}")
                        
            st.divider()
else:
    st.warning("El catálogo está vacío. Asegúrate de haber pegado correctamente tu API Key.")
