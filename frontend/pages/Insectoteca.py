import streamlit as st
import mysql.connector

# Función para obtener la información detallada de un insecto y sus relaciones
def obtener_informacion_insecto(insecto):
    cursor.execute("""
        SELECT 
            i.NOMBRE,
            i.DESCRIPCION,
            i.DISTRIBUCION_GEO,
            i.ESTADO_CONSERVACION,
            i.LINK_IMAGEN,
            c.NOMBRE AS clase,
            d.DIETA_ID AS dieta,
            d.TIPO as TIPO,
            d.CONSUMIDO AS COMSUMO,
            d.PREFERENCIAS_ALIMENTACION as PREFE,
            d.PATRONES_ALIMENTACION as PATRON,
            h.HABITAT_ID AS habitat,
            h.TIPO AS TIPO_A,
            h.DESCRIPCION AS DES_H,
            h.TEMPERATURA AS TEMP,
            h.HUMEDAD AS HUM,
            h.ALTITUD AS ALT,
            h.PRECIPITACION AS PRECIP,
            h.OTROS_FACTORES AS OF,
            cv.CICLO_VIDA_ID AS ciclo_vida,
            cv.ETAPAS AS E,
            cv.DURACION AS DUR,
            cv.DESCRIPCION AS DESCRIP,
            cv.FACTORES AS FAC,
            cv.COMPORTAMIENTOS as COM
        FROM 
            insecto AS i
        INNER JOIN 
            clase AS c ON i.CLASE_ID = c.CLASE_ID
        INNER JOIN 
            dieta AS d ON i.DIETA_ID = d.DIETA_ID
        INNER JOIN 
            habitat AS h ON i.HABITAT_ID = h.HABITAT_ID
        INNER JOIN 
            ciclo_vida AS cv ON i.CLICLO_ID = cv.CICLO_VIDA_ID
        WHERE 
            i.NOMBRE = %s
    """, (insecto,))
    return cursor.fetchone()

# Conexión a la base de datos MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="insect_db"
)
cursor = conn.cursor()

# Consulta para obtener la lista de insectos
cursor.execute("SELECT NOMBRE FROM insecto")
insectos = cursor.fetchall()

# Lista de insectos como opciones para seleccionar
insectos_list = [insecto[0] for insecto in insectos]

st.sidebar.markdown("<br>", unsafe_allow_html=True)

# Sidebar para seleccionar un insecto
selected_insecto = st.sidebar.selectbox("Selecciona un insecto", insectos_list)

# Mostrar información detallada del insecto seleccionado
insecto_info = obtener_informacion_insecto(selected_insecto)
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
if insecto_info:
    nombre, descripcion, distribucion_geo, estado_conservacion, imagen_ruta, clase, dieta,tipo,consumo,prefe,patron, habitat, tipo_a,desh,temp,hum,alt,precip,of,ciclo_vida,eta,dur,desc,fact,comportamiento = insecto_info
    st.markdown(custom_css, unsafe_allow_html=True)
    st.header(nombre, divider='rainbow')
    #st.title(nombre)
    st.image(imagen_ruta, caption=nombre, use_column_width=True)
    st.write("DESCRIPCIÓN:", descripcion)
    st.write("DISTRIBUCIÓN GEOGRAFICA:", distribucion_geo)
    st.write("ESTADO DE CONSEVACIÓN:", estado_conservacion) 
    st.divider()
    st.markdown("<div class='titulos'>Clase</div>",  unsafe_allow_html=True)
    st.write("Clase: ", clase)
    st.divider()
    st.markdown("<div class='titulos'>Dieta</div>",  unsafe_allow_html=True) 
    st.write("TIPO DE DIETA: ", tipo)
    st.write("COMSUMO: ", consumo)
    st.write("PREFERENCIA DE ALIMENTACIÓN: ", prefe)
    st.write("PATRONES DE ALIMENTACIÓN: ", patron)
    st.divider()
    st.markdown("<div class='titulos'>Habitat</div>",  unsafe_allow_html=True) 
    st.write("TIPO DE HABITAT:", tipo_a)
    st.write("DESCRIPCIÓN:", desh)
    st.write("TEMPERATURA:", temp)
    st.write("HUMEDAD:", hum)
    st.write("ALTITUD:", alt)
    st.write("PRECIPITACIÓN:", precip)
    st.write("OTROS FACTORES:", of)
    st.divider()
    st.markdown("<div class='titulos'>Ciclo de vida</div>",  unsafe_allow_html=True) 
    st.write("ETAPAS: ", eta)
    st.write("DURACIÓN: ", dur)
    st.write("DESCRIPCIÓN: ", desc)
    st.write("FACTORES: ", fact)
    st.write("COMPORTAMIENTOS:", comportamiento)
    
     # Línea vertical separadora
    st.markdown("<div class='separator'></div>", unsafe_allow_html=True)

    # Footer
    st.markdown("<div class='footer'>Hecho con Streamlit - Desarrollado por Estudiantes Especializacion IA UOA @2024-1</div>", unsafe_allow_html=True)
else:
    st.warning("No se encontró información para el insecto seleccionado.")
    
     # Línea vertical separadora
    st.markdown("<div class='separator'></div>", unsafe_allow_html=True)

    # Footer
    st.markdown("<div class='footer'>Hecho con Streamlit - Desarrollado por Estudiantes Especializacion IA UOA @2024-1</div>", unsafe_allow_html=True)
#eta,dur,desc,fact,comportamiento
# Cerrar conexión a la base de datos
cursor.close()
conn.close()
