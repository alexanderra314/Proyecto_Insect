import streamlit as st
from streamlit_folium import folium_static
import folium
import mysql.connector

    

# Conexión a la base de datos MySQL
def connect_to_database():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="insect_db"
    )

# Función para obtener los hallazgos de la base de datos
def get_discoveries():
    connection = connect_to_database()
    cursor = connection.cursor()
    cursor.execute("SELECT geo_inset_id, titulo, descripcion, user, fecha, lat, log FROM geo_insect WHERE lat IS NOT NULL AND log IS NOT NULL")
    discoveries = cursor.fetchall()
    connection.close()
    return discoveries

# Función para mostrar los hallazgos en el mapa
def show_discoveries_map(discoveries):
    if discoveries:
        map_center = [sum([float(discovery[5]) for discovery in discoveries]) / len(discoveries), 
              sum([float(discovery[6]) for discovery in discoveries]) / len(discoveries)]
        map_zoom = 2
        m = folium.Map(location=map_center, zoom_start=map_zoom, control_scale=True)
        for discovery in discoveries:
            folium.Marker([discovery[5], discovery[6]], popup=f"Título: {discovery[1]}, Descripción: {discovery[2]}, Usuario: {discovery[3]}, Fecha: {discovery[4]}").add_to(m)
        folium_static(m)
    else:
        st.write("No hay hallazgos con coordenadas registradas en la base de datos.")

# Función principal de la aplicación
def main():
    st.set_page_config(
        page_title='Home Page', 
        page_icon='🌍', 
        layout='centered', 
        initial_sidebar_state='auto'
    )
    
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
    st.header('Mapa de Hallazgos de Insectos', divider='rainbow')  
    st.markdown("<div class='container'> Aqui observaremos todos los insecto que se han reportado. </div>",  unsafe_allow_html=True)


    # Página para ver los hallazgos existentes en el mapa
    discoveries = get_discoveries()
    show_discoveries_map(discoveries)

    # Footer
    st.markdown("<div class='footer'>Hecho con Streamlit - Desarrollado por Estudiantes Especializacion IA UOA @2024-1</div>", unsafe_allow_html=True)

# Ejecutar la función principal
if __name__ == "__main__":
    main()
