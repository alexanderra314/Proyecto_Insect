import streamlit as st


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
    st.header('Entorno de Trabajo', divider='rainbow')  
    st.divider()
    #
    
    st.markdown("<div class='titulos'> Ing. Edward Trejos </div>",  unsafe_allow_html=True)
    st.markdown("<div class='titulos'> Ing. Kuis E. Mantilla </div>",  unsafe_allow_html=True)
    st.markdown("<div class='titulos'> Ing. Alexander Rodriguez </div>",  unsafe_allow_html=True)
    st.divider()
    st.markdown("<div class='titulos'> Roles </div>",  unsafe_allow_html=True)
    
    txt = st.text_area(
        "   Líder del Proyecto:", 
        "•	Responsable de la gestión general del proyecto.\n"
        "•	Coordinar las actividades del equipo y se asegura de que se cumplan los plazos.\n"
        "•	Punto de contacto principal para la comunicación con el cliente y la gestión de expectativas",
    )
    
    txt = st.text_area(
        "   Scrum Master:", 
        "•	Facilita las reuniones diarias, las reuniones de planificación de sprint, las revisiones de sprint y las retrospectivas para garantizar que se sigan las prácticas ágiles de Scrum.\n"
        "•  Ayuda al equipo a eliminar obstáculos y resolver problemas que puedan surgir durante el desarrollo del proyecto.\n"
        "•	Fomenta la colaboración, la comunicación y la transparencia dentro del equipo."
        "•	Trabaja en estrecha colaboración con el Product Owner para priorizar y gestionar el backlog del producto",
    )
    txt = st.text_area(
        "   Product Owner:", 
        "•	Representa los intereses del cliente y del negocio.\n"
        "•	Define y prioriza los requisitos del producto en el backlog del producto.\n"
        "•	Trabaja en estrecha colaboración con el equipo de desarrollo para garantizar que se entreguen funcionalidades valiosas y que se cumplan las expectativas del cliente.",
    )
    
    txt = st.text_area(
        "   Desarrollador de Backend:", 
        "•	Encargado del desarrollo del backend de la aplicación.\n"
        "•	Diseña y desarrolla la lógica del servidor y la base de datos.\n"
        "•	Se asegura de que la aplicación tenga un rendimiento óptimo y sea escalable.",
    )
    
    txt = st.text_area(
        "   Desarrollador de Frontend:", 
        "•	Responsable del desarrollo de la interfaz de usuario de la aplicación móvil.\n"
        "•	Responsable de diseñar la experiencia de usuario y la interfaz de usuario de la aplicación.\n"
        "•	Trabaja en estrecha colaboración con el equipo de diseño para garantizar una interfaz intuitiva y atractiva.",
    )
    
    
    txt = st.text_area(
        "   Diseñador UX/UI:", 
        "•	Diseña y desarrolla la experiencia de usuario (UX/UI) de la aplicación.\n"
        "•	Trabaja en estrecha colaboración con el desarrollador frontend para implementar diseños atractivos y funcionales.",
    )
    
    txt = st.text_area(
        "   Especialista en Machine Learning:", 
        "•	Encargado de desarrollar y entrenar el modelo de inteligencia artificial para la clasificación de insectos.\n"
        "•	Colabora con el equipo de desarrollo para integrar el modelo de IA en la aplicación móvil.\n"
        "•	Selecciona y ajusta algoritmos de machine learning para lograr la precisión deseada en la identificación de insectos.",
    )
    
    txt = st.text_area(
        "   Especialista en Biodiversidad/Entomología:", 
        "•	Proporciona conocimientos especializados sobre la clasificación de insectos y la biodiversidad.\n"
        "•	Ayuda en la recopilación de datos y en la validación del modelo de inteligencia artificial.\n"
        "•	Contribuye a la redacción de contenidos educativos sobre los insectos para la aplicación.",
    )
    
    txt = st.text_area(
        "   DevOps Engineer:", 
        "•	Encargado de diseñar, implementar y mantener la infraestructura en la nube para la aplicación.\n"
        "•	Configura herramientas de despliegue continuo, monitoreo y seguridad en la nube.\n"
        "•	Colabora con el equipo de desarrollo para garantizar un despliegue eficiente y escalable de la aplicación.",
    )
    
    
    st.markdown("<div class='titulos'> Canales de Comunicación </div>",  unsafe_allow_html=True)
    
    txt = st.text_area(
        "   Reuniones periódicas:", 
        "   Reuniones periódicas para actualizar el progreso, discutir los desafíos y tomar decisiones importantes del proyecto.",
    )
    
    txt = st.text_area(
        "   Plataforma de colaboración:", 
        "   Utilizar herramientas como Slack, Microsoft Teams para la comunicación diaria, compartir archivos y discutir ideas de manera rápida y eficiente.",
    )
    
    txt = st.text_area(
        "   Tablero de Proyectos:", 
        "   Herramienta de gestión de proyectos como Trello, Azure DevOps para mantener un registro de las tareas pendientes, asignar responsabilidades y hacer un seguimiento del progreso.",
    )
    
    txt = st.text_area(
        "   Correo electrónico:", 
        "   Utilizar el correo electrónico para comunicaciones formales, compartir documentos importantes y coordinar reuniones.",
    )
    
    st.markdown("<div class='Metodología de trabajo'> Roles </div>",  unsafe_allow_html=True)
    
    txt = st.text_area(
        " Utilizamos Scrum porque es un marco de trabajo ágil que permite una entrega rápida y flexible de productos de alta calidad al cliente. Scrum promueve la transparencia, la colaboración y la adaptación continua, lo que ayuda a los equipos a responder de manera efectiva a los cambios en los requisitos del proyecto y a mantener un enfoque centrado en el valor del negocio.",
    )
    
     # Línea vertical separadora
    st.markdown("<div class='separator'></div>", unsafe_allow_html=True)

    # Footer
    st.markdown("<div class='footer'>Hecho con Streamlit - Desarrollado por Estudiantes Especializacion IA UOA @2024-1</div>", unsafe_allow_html=True)

if __name__ == '__main__':
    app()