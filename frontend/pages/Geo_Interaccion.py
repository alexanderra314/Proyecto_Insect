import streamlit as st
from streamlit_folium import folium_static
import folium
import mysql.connector
import pyperclip

# Conexión a la base de datos MySQL
def connect_to_database():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="insect_db"
    )

# Función para insertar un nuevo hallazgo en la base de datos
def insert_discovery(title, description, user, latitude, longitude, date):
    connection = connect_to_database()
    cursor = connection.cursor()
    query = "INSERT INTO `geo_insect`( `user`, `descripcion`, `titulo`, `lat`, `log`, `fecha`)  VALUES (%s, %s, %s, %s, %s, %s)"
    data = (user, description, title, str(latitude), str(longitude), date)
    cursor.execute(query, data)
    connection.commit()
    connection.close()

# Función principal de la aplicación
def main():
    custom_css = """
        <style>
            body {
                background-color: #f0f0f0; /* Color de fondo general */
            }
            .container{
                text-align: center;
                font-size: 14px;
            }
            .titulos{
                text-align: center;
                font-size: 28px;
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
            
        </style>
    """
    st.markdown(custom_css, unsafe_allow_html=True)
    st.header('Plataforma de Ubicación Hallazgos.', divider='rainbow')
    st.markdown("<div class='container'> Aqui prodras ubicar Geograficamente tus hallazgos </div>",  unsafe_allow_html=True)
    st.divider()

    # Sección para que los usuarios añadan un nuevo hallazgo con ubicación
    title = st.text_input("Título del Hallazgo:")
    description = st.text_area("Descripción:")
    user = st.text_input("Nombre del Usuario:")
    date = st.date_input("Fecha del Hallazgo:")
    
    # Mapa interactivo para seleccionar las coordenadas
    st.header("Seleccionar Ubicación en el Mapa")
    map_center = [0, 0]  # Coordenadas iniciales del mapa
    map_zoom = 2  # Nivel de zoom inicial del mapa
    m = folium.Map(location=map_center, zoom_start=map_zoom, control_scale=True)
    m.add_child(folium.ClickForLatLng(format_str='"[" + lat + "," + lng + "]"', alert=False))
    location = folium.LatLngPopup()  # Permitir al usuario hacer clic en el mapa para seleccionar una ubicación
    m.add_child(location)
    folium_static(m)



        
    if st.button("Guardar Hallazgo"): 
            coordinates = pyperclip.paste() 
            if coordinates:
                latitude, longitude = map(float, coordinates.strip("[]").split(','))
                insert_discovery(title, description, user, latitude, longitude, date)
                st.success("¡Hallazgo guardado con éxito!")
            else:
                st.warning("Por favor, selecciona una ubicación en el mapa antes de guardar el hallazgo.")

    st.markdown("<div class='separator'></div>", unsafe_allow_html=True)

    # Footer
    st.markdown("<div class='footer'>Hecho con Streamlit - Desarrollado por Estudiantes Especializacion IA UOA @2024-1</div>", unsafe_allow_html=True)


# Ejecutar la función principal
if __name__ == "__main__":
    main()