import streamlit as st

def contenido_educativo():
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
    st.header("Contenido Educativo sobre Insectos y su Rol en los Ecosistemas", divider='rainbow')

    st.subheader("Artículos:")
    st.markdown("- [Importancia de los insectos en losAgricultura](https://www.mag.go.cr/bibliotecavirtual/H10-10951.pdf)")
    st.markdown("- [Los insectos y su papel en la Bitecnologia](https://www.inecol.mx/inecol/index.php/es/ct-menu-item-25/ct-menu-item-27/17-ciencia-hoy/1785-los-insectos-fuente-de-innovaciones-biotecnologicas)")
    st.markdown("- [Atlas de los insectos](https://www.tierra.org/wp-content/uploads/2020/12/Atlas-Insectos-Amigos-Tierra-2020.pdf)")

    st.subheader("Videos:")
    st.video("https://www.youtube.com/watch?v=AKdKM643QSo")

    st.subheader("Infografías:")
    
         # Línea vertical separadora
    st.markdown("<div class='separator'></div>", unsafe_allow_html=True)

    # Footer
    st.markdown("<div class='footer'>Hecho con Streamlit - Desarrollado por Estudiantes Especializacion IA UOA @2024-1</div>", unsafe_allow_html=True)

if __name__ == "__main__":
    contenido_educativo()
