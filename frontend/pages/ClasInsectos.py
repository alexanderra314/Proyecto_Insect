import streamlit as st
from PIL import Image
import requests 
import os
import shutil




API_URL = os.getenv('API_URL', 'http://localhost:8080')
def llamar_api(image_file):
    url = f"{API_URL}/insect-model/predict"

 
    files = {"file": image_file}
    response = requests.post(url, files=files) 
    #print('repuesta '+response)
    if response.status_code == 200:
        #predictions = response.json()["predictions"]
        st.write("Predicciones:")
        image_path = r'C:/Users/alexa/runs/detect/predict/temp.jpg'
        if os.path.exists(image_path):
            st.image(image_path, caption='Imagen seleccionada', use_column_width=True)
        else:
            st.warning('La imagen no se encontró en la carpeta especificada')
    else:
        st.warning('No se pudo Clasificar la imagen')
        
def eliminar_carpeta_detect():
    try:
        shutil.rmtree(r'C:/Users/alexa/runs/detect/predict')
    except FileNotFoundError:
        st.warning('La carpeta "detect" no existe.')
    except Exception as e:
        st.error(f'Error al eliminar la carpeta "detect": {e}')

        
def redirect_to_geo_interaccion():
    js_redirect_code = """
    <script>
    window.location.href = '/Geo_Interaccion'
    </script>
    """
    st.components.v1.html(js_redirect_code)

def app():

    st.set_page_config(
        page_title='Home Page', 
        page_icon='🌍', 
        layout='centered', 
        initial_sidebar_state='auto'
    )

    # Estilo CSS para el fondo y colores de las secciones
    custom_css = """
        <style>
            body {
                background-color: #f0f0f0; /* Color de fondo general */
            }
            .container{
                text-align: center;
                font-size: 14px;
            }
            .header {
                font-family: "Source Sans Pro", sans-serif;
                color: rgb(49, 51, 63);
                line-height: 1.2;
                font-size: 2.25rem;
                text-align: center; 
            #background-color: black; /* Color de fondo del encabezado */
            #padding: 22px;
            #border-radius: 10px;
            #color: white; /* Color del texto */
            #text-align: center; /* Alineación del texto */
            #margin-bottom: 60px;
            #width: 100%;
            }
            
            #.left-section {
            #    background-color: #ffffff; /* Color de fondo de la sección izquierda */
            #    padding: 0px;
            #    border-radius: 10px;
            #    #float: left;
            #    width: 100%;
            #}
            .right-section {
                background-color: #ffffff; /* Color de fondo de la sección derecha */
                padding: 20px;
                border-radius: 10px;
            }

            .footer {
                position: fixed;
                bottom: 0;
                left: 0;
                width: 100%;
                background-color: #f0f0f0;
                padding: 10px 20px;
                text-align: center;
                font-size: 14px;
                color: #333;
                border-top: 1px solid #ccc;
            }
            .link-button {
            background-color: transparent;
            border: none;
            color: blue;
            text-decoration: underline;
            cursor: pointer;
            font-size: 14px;
            padding: 0;
            }
            
        </style>
    """
# Insertar el CSS para el fondo y colores de las secciones
    st.markdown(custom_css, unsafe_allow_html=True)
    st.header('Explora y Clasifica la Fauna Insectívora', divider='rainbow')
    st.markdown("<div class='container'> ¡Bienvenido a nuestra plataforma de clasificación de insectos! Sumérgete en el fascinante mundo de la entomología y experimenta la emoción de explorar la diversidad de los insectos a través de nuestro innovador modelo de clasificación. Con nuestra herramienta, no solo podrás aprender sobre diferentes especies de insectos, sino que también tendrás la oportunidad de contribuir al conocimiento científico mediante la identificación y clasificación de especímenes. </div>",  unsafe_allow_html=True)
    st.divider()

    left_section, right_section = st.columns(2)
    
    # Columna 1: Subir imagen
    with left_section:
        st.markdown("<h3 style='text-align: center; color: blue;'>Vamos a Carga una imagen:</h3>", unsafe_allow_html=True)

        uploaded_file = st.file_uploader("Cargar imagen", type=["jpg", "png", "jpeg"])

        # Validar la extensión del archivo
        if uploaded_file is not None:
            file_extension = uploaded_file.name.split(".")[-1]
            if file_extension.lower() not in ["jpg", "jpeg", "png"]:
                #st.error("La imagen debe ser de tipo JPG, JPEG o PNG.")
                st.warning('La imagen debe ser de tipo JPG, JPEG o PNG.', icon="⚠️")
            else:
                #image = Image.open(uploaded_file)
                st.image(uploaded_file, caption="Imagen seleccionada", use_column_width=True)
        
  
        is_clicked = st.button('Clasificar')
        if is_clicked:
            if uploaded_file is not None:
                eliminar_carpeta_detect()
                llamar_api(uploaded_file)
            else:
                st.warning('Por favor carga una imagen antes de clasificar.')
            
            

    col1, col2 = st.columns(2)

    # Columna 1: Botón para registrar ubicación
    with col1:
        st.markdown("<h2 style='text-align: left; color: black; font-size: 14px;'><a href='/Geo_Interaccion'>Quieres Compartir tus Hallazgos</a></h2>", unsafe_allow_html=True)

    
    # Columna 2: Botón para compartir hallazgos
    with col2:
        st.markdown("<h2 style='text-align: left; color: black; font-size: 14px;'><a href='/Interaccion_participativa'>Quieres Compartir tu Experiencia</a></h2>", unsafe_allow_html=True)

    
     # Línea vertical separadora
    st.markdown("<div class='separator'></div>", unsafe_allow_html=True)

    # Footer
    st.markdown("<div class='footer'>Hecho con Streamlit - Desarrollado por Estudiantes Especializacion IA UOA @2024-1</div>", unsafe_allow_html=True)

if __name__ == '__main__':
    app()
