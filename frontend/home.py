import streamlit as st
#streamlit run home.py
def app():
    
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
   
    st.header('Identificación Inteligente de Insectos.', divider='rainbow')

    st.markdown("<div class='container'> vamos a Desarrollar una aplicación web amigable con el usuario que emplee inteligencia artificial (IA) para identificar con precisión y proporcionar información detallada sobre diversos insectos a partir de fotografías tomadas o cargadas por los usuarios. </div>",  unsafe_allow_html=True)
    st.markdown("<div class='container'> La aplicación tiene como  objetivo promover la conciencia sobre la biodiversidad, asistir en la investigación científica y comprometer a los usuarios en proyectos de ciencia ciudadana </div>",  unsafe_allow_html=True)

    st.divider()
    
    st.markdown("<div class='titulos'> Ing. Edward Trejos </div>",  unsafe_allow_html=True)
    st.markdown("<div class='titulos'> Ing. Luis E. Mantilla </div>",  unsafe_allow_html=True)
    st.markdown("<div class='titulos'> Ing. Alexander Rodriguez </div>",  unsafe_allow_html=True)

    st.markdown("<div class='separator'></div>", unsafe_allow_html=True)


    st.markdown("<div class='footer'>Hecho con Streamlit - Desarrollado por Estudiantes Especializacion IA UOA @2024-1</div>", unsafe_allow_html=True)


if __name__ == '__main__':
    app()
