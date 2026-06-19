import streamlit as st
import requests

# --- CONFIGURACIÓN DE LA PÁGINA MÓVIL ---
st.set_page_config(page_title="Panel CEO", page_icon="📱", layout="centered")

# Enlace de Make (Simulador por ahora)
MAKE_WEBHOOK_URL = "https://hook.us2.make.com/7gwzs8q25amgf72xlpwatafvhgfvgal3"

# Simulador de los productos recomendados por la IA
# Simulador con imágenes reales (.jpg) para pasar el estricto filtro de Instagram
productos_encontrados = [
    {"nombre": "Cama Nube Mascotas", "costo": 12.00, "envio": 2.50, "img": "https://www.google.com/search?q=imagenes+de+arboles&sca_esv=06ebad7ca6d3d30d&sxsrf=APpeQnvCJ4uOEYgQyF03dvWDPUFFE6S3UA%3A1781903004123&source=hp&ei=nK41aonlBIfckvQP956F-A0&iflsig=ABILxe8AAAAAajW8rNT4T7EQ9MT9yGZJY8QV4dPUQxyl&ved=0ahUKEwiJo9T8mZSVAxUHroQIHXdPAd8Q4dUDCDo&uact=5&oq=imagenes+de+arboles&gs_lp=Egdnd3Mtd2l6IhNpbWFnZW5lcyBkZSBhcmJvbGVzMgUQABiABDIFEAAYgAQyBRAAGIAEMgUQABiABDIFEAAYgAQyBRAAGIAEMgUQABiABDIFEAAYgAQyBRAAGIAEMgUQABiABEjfE1AAWJsTcAB4AJABAJgBtQGgAakRqgEEMC4xOLgBA8gBAPgBAZgCEqAC5hPCAgoQIxiABBiKBRgnwgIQECMY8AUYyQIYgAQYigUYJ8ICBBAjGCfCAgsQABiABBixAxiDAcICDhAAGIAEGIoFGLEDGIMBwgILEC4YgAQYsQMYgwHCAggQABiABBixA8ICDhAuGIAEGLEDGMcBGNEDwgILEC4YgAQYxwEY0QPCAhAQIxjJAhjwBRiABBiKBRgnwgIEEAAYA5gDAJIHBjAuMTcuMaAH0G-yBwYwLjE3LjG4B-YTwgcIMi0yLjE0LjLIB4gCgAgB&sclient=gws-wiz#sv=CAMSZxowKg5KVUhtMUlLME5ZRjFvTTIOSlVIbTFJSzBOWUYxb006DmM0bWViYXVrZzIzRUxNIAQqLwobX29LNDFhdkNrRnZTTXdia1B3cWJ5dUFNXzQ1Eg5KVUhtMUlLME5ZRjFvTRgAMAEYByCIifHOAUoIEAEYASABKAE"},
    {"nombre": "Humidificador Llama", "costo": 15.00, "envio": 0.00, "img": "https://www.google.com/search?q=imagenes+de+arboles&sca_esv=06ebad7ca6d3d30d&sxsrf=APpeQnvCJ4uOEYgQyF03dvWDPUFFE6S3UA%3A1781903004123&source=hp&ei=nK41aonlBIfckvQP956F-A0&iflsig=ABILxe8AAAAAajW8rNT4T7EQ9MT9yGZJY8QV4dPUQxyl&ved=0ahUKEwiJo9T8mZSVAxUHroQIHXdPAd8Q4dUDCDo&uact=5&oq=imagenes+de+arboles&gs_lp=Egdnd3Mtd2l6IhNpbWFnZW5lcyBkZSBhcmJvbGVzMgUQABiABDIFEAAYgAQyBRAAGIAEMgUQABiABDIFEAAYgAQyBRAAGIAEMgUQABiABDIFEAAYgAQyBRAAGIAEMgUQABiABEjfE1AAWJsTcAB4AJABAJgBtQGgAakRqgEEMC4xOLgBA8gBAPgBAZgCEqAC5hPCAgoQIxiABBiKBRgnwgIQECMY8AUYyQIYgAQYigUYJ8ICBBAjGCfCAgsQABiABBixAxiDAcICDhAAGIAEGIoFGLEDGIMBwgILEC4YgAQYsQMYgwHCAggQABiABBixA8ICDhAuGIAEGLEDGMcBGNEDwgILEC4YgAQYxwEY0QPCAhAQIxjJAhjwBRiABBiKBRgnwgIEEAAYA5gDAJIHBjAuMTcuMaAH0G-yBwYwLjE3LjG4B-YTwgcIMi0yLjE0LjLIB4gCgAgB&sclient=gws-wiz#sv=CAMSZxowKg5KVUhtMUlLME5ZRjFvTTIOSlVIbTFJSzBOWUYxb006DmM0bWViYXVrZzIzRUxNIAQqLwobX29LNDFhdkNrRnZTTXdia1B3cWJ5dUFNXzQ1Eg5KVUhtMUlLME5ZRjFvTRgAMAEYByCIifHOAUoIEAEYASABKAE"},
    {"nombre": "Corrector Postura", "costo": 8.00, "envio": 1.50, "img": "https://www.google.com/search?q=imagenes+de+arboles&sca_esv=06ebad7ca6d3d30d&sxsrf=APpeQnvCJ4uOEYgQyF03dvWDPUFFE6S3UA%3A1781903004123&source=hp&ei=nK41aonlBIfckvQP956F-A0&iflsig=ABILxe8AAAAAajW8rNT4T7EQ9MT9yGZJY8QV4dPUQxyl&ved=0ahUKEwiJo9T8mZSVAxUHroQIHXdPAd8Q4dUDCDo&uact=5&oq=imagenes+de+arboles&gs_lp=Egdnd3Mtd2l6IhNpbWFnZW5lcyBkZSBhcmJvbGVzMgUQABiABDIFEAAYgAQyBRAAGIAEMgUQABiABDIFEAAYgAQyBRAAGIAEMgUQABiABDIFEAAYgAQyBRAAGIAEMgUQABiABEjfE1AAWJsTcAB4AJABAJgBtQGgAakRqgEEMC4xOLgBA8gBAPgBAZgCEqAC5hPCAgoQIxiABBiKBRgnwgIQECMY8AUYyQIYgAQYigUYJ8ICBBAjGCfCAgsQABiABBixAxiDAcICDhAAGIAEGIoFGLEDGIMBwgILEC4YgAQYsQMYgwHCAggQABiABBixA8ICDhAuGIAEGLEDGMcBGNEDwgILEC4YgAQYxwEY0QPCAhAQIxjJAhjwBRiABBiKBRgnwgIEEAAYA5gDAJIHBjAuMTcuMaAH0G-yBwYwLjE3LjG4B-YTwgcIMi0yLjE0LjLIB4gCgAgB&sclient=gws-wiz#sv=CAMSZxowKg5KVUhtMUlLME5ZRjFvTTIOSlVIbTFJSzBOWUYxb006DmM0bWViYXVrZzIzRUxNIAQqLwobX29LNDFhdkNrRnZTTXdia1B3cWJ5dUFNXzQ1Eg5KVUhtMUlLME5ZRjFvTRgAMAEYByCIifHOAUoIEAEYASABKAE"},
    {"nombre": "Cepillo Quita Pelos", "costo": 4.00, "envio": 4.50, "img": "https://www.google.com/search?q=imagenes+de+arboles&sca_esv=06ebad7ca6d3d30d&sxsrf=APpeQnvCJ4uOEYgQyF03dvWDPUFFE6S3UA%3A1781903004123&source=hp&ei=nK41aonlBIfckvQP956F-A0&iflsig=ABILxe8AAAAAajW8rNT4T7EQ9MT9yGZJY8QV4dPUQxyl&ved=0ahUKEwiJo9T8mZSVAxUHroQIHXdPAd8Q4dUDCDo&uact=5&oq=imagenes+de+arboles&gs_lp=Egdnd3Mtd2l6IhNpbWFnZW5lcyBkZSBhcmJvbGVzMgUQABiABDIFEAAYgAQyBRAAGIAEMgUQABiABDIFEAAYgAQyBRAAGIAEMgUQABiABDIFEAAYgAQyBRAAGIAEMgUQABiABEjfE1AAWJsTcAB4AJABAJgBtQGgAakRqgEEMC4xOLgBA8gBAPgBAZgCEqAC5hPCAgoQIxiABBiKBRgnwgIQECMY8AUYyQIYgAQYigUYJ8ICBBAjGCfCAgsQABiABBixAxiDAcICDhAAGIAEGIoFGLEDGIMBwgILEC4YgAQYsQMYgwHCAggQABiABBixA8ICDhAuGIAEGLEDGMcBGNEDwgILEC4YgAQYxwEY0QPCAhAQIxjJAhjwBRiABBiKBRgnwgIEEAAYA5gDAJIHBjAuMTcuMaAH0G-yBwYwLjE3LjG4B-YTwgcIMi0yLjE0LjLIB4gCgAgB&sclient=gws-wiz#sv=CAMSZxowKg5KVUhtMUlLME5ZRjFvTTIOSlVIbTFJSzBOWUYxb006DmM0bWViYXVrZzIzRUxNIAQqLwobX29LNDFhdkNrRnZTTXdia1B3cWJ5dUFNXzQ1Eg5KVUhtMUlLME5ZRjFvTRgAMAEYByCIifHOAUoIEAEYASABKAE"},
    {"nombre": "Lámpara Galaxia", "costo": 18.00, "envio": 3.00, "img": "https://www.google.com/search?q=imagenes+de+arboles&sca_esv=06ebad7ca6d3d30d&sxsrf=APpeQnvCJ4uOEYgQyF03dvWDPUFFE6S3UA%3A1781903004123&source=hp&ei=nK41aonlBIfckvQP956F-A0&iflsig=ABILxe8AAAAAajW8rNT4T7EQ9MT9yGZJY8QV4dPUQxyl&ved=0ahUKEwiJo9T8mZSVAxUHroQIHXdPAd8Q4dUDCDo&uact=5&oq=imagenes+de+arboles&gs_lp=Egdnd3Mtd2l6IhNpbWFnZW5lcyBkZSBhcmJvbGVzMgUQABiABDIFEAAYgAQyBRAAGIAEMgUQABiABDIFEAAYgAQyBRAAGIAEMgUQABiABDIFEAAYgAQyBRAAGIAEMgUQABiABEjfE1AAWJsTcAB4AJABAJgBtQGgAakRqgEEMC4xOLgBA8gBAPgBAZgCEqAC5hPCAgoQIxiABBiKBRgnwgIQECMY8AUYyQIYgAQYigUYJ8ICBBAjGCfCAgsQABiABBixAxiDAcICDhAAGIAEGIoFGLEDGIMBwgILEC4YgAQYsQMYgwHCAggQABiABBixA8ICDhAuGIAEGLEDGMcBGNEDwgILEC4YgAQYxwEY0QPCAhAQIxjJAhjwBRiABBiKBRgnwgIEEAAYA5gDAJIHBjAuMTcuMaAH0G-yBwYwLjE3LjG4B-YTwgcIMi0yLjE0LjLIB4gCgAgB&sclient=gws-wiz#sv=CAMSZxowKg5KVUhtMUlLME5ZRjFvTTIOSlVIbTFJSzBOWUYxb006DmM0bWViYXVrZzIzRUxNIAQqLwobX29LNDFhdkNrRnZTTXdia1B3cWJ5dUFNXzQ1Eg5KVUhtMUlLME5ZRjFvTRgAMAEYByCIifHOAUoIEAEYASABKAE"}
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
                # AQUÍ ESTÁ EL PAQUETE JSON COMPLETO
                datos_para_ia = {
                    "producto": prod["nombre"], 
                    "precio": f"${precio_venta:.2f}",
                    "imagen_url": prod["img"]
                }
                
                try:
                    requests.post(MAKE_WEBHOOK_URL, json=datos_para_ia)
                    st.success(f"¡Orden ejecutada! La IA está creando anuncios para {prod['nombre']}.")
                except Exception as e:
                    st.error(f"Fallo en la conexión: {e}")
                    
        st.divider()
