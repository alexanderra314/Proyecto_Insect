import streamlit as st
import mysql.connector

# Conexión a la base de datos MySQL
def connect_to_database():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="insect_db"
    )

# Función para insertar un nuevo hallazgo en la base de datos
def insert_discovery(title, description, user,date):
    connection = connect_to_database()
    cursor = connection.cursor()
    query = "INSERT INTO interaccion_usuario (titulo, descricion, user, fecha) VALUES (%s, %s, %s,%s)"
    data = (title, description, user,date)
    cursor.execute(query, data)
    connection.commit()
    connection.close()

# Función para mostrar los hallazgos almacenados en la base de datos
def show_discoveries():
    connection = connect_to_database()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM interaccion_usuario")
    discoveries = cursor.fetchall()
    connection.close()
    return discoveries

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
    st.header("Plataforma de Hallazgos Científicos", divider='rainbow')

    # Sección para que los usuarios añadan un nuevo hallazgo
    title = st.text_input("Título del Hallazgo:")
    description = st.text_area("Descripción:")
    user = st.text_input("Tu Nombre:")
    date = st.date_input("Fecha del Hallazgo:")
    if st.button("Guardar Hallazgo"):
        insert_discovery(title, description, user,date)
        st.success("¡Hallazgo guardado con éxito!")

    # Sección para mostrar los hallazgos almacenados

    st.header("Hallazgos Guardados", divider='rainbow')
    discoveries = show_discoveries()
    for discovery in discoveries:
        st.write(f"**Título:** {discovery[1]}")
        st.write(f"**Descripción:** {discovery[2]}")
        st.write(f"**Usuario:** {discovery[3]}")
        st.markdown("---")
        
         # Línea vertical separadora
    st.markdown("<div class='separator'></div>", unsafe_allow_html=True)

    # Footer
    st.markdown("<div class='footer'>Hecho con Streamlit - Desarrollado por Estudiantes Especializacion IA UOA @2024-1</div>", unsafe_allow_html=True)

# Ejecutar la función principal
if __name__ == "__main__":
    main()
