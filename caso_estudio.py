import streamlit as st

def mostrar_caso_estudio():
    st.title("Caso de estudio: análisis de los diferentes tipos de datos")
    
    # Volver a un enfoque simple para evitar problemas de renderizado
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div style="background-color: #f8f9fa; padding: 15px; border-radius: 8px; box-shadow: 0 2px 5px rgba(0,0,0,0.1);">
            <h3 style="color: #2c5282; margin-top: 0; border-bottom: 2px solid #e2e8f0; padding-bottom: 10px;">Estudiantes:</h3>
            <p style="margin: 8px 0; font-size: 16px;">Duvan Arley Botero</p>
            <p style="margin: 8px 0; font-size: 16px;">Daniel Felipe Marin</p>
            <p style="margin: 8px 0; font-size: 16px;">Angelo Duque</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div style="background-color: #f8f9fa; padding: 15px; border-radius: 8px; box-shadow: 0 2px 5px rgba(0,0,0,0.1); margin-top: 15px;">
            <h3 style="color: #2c5282; margin-top: 0; border-bottom: 2px solid #e2e8f0; padding-bottom: 10px;">Docente:</h3>
            <p style="margin: 8px 0; font-size: 16px;">Aharon Alexander Aguas</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div style="background-color: #f8f9fa; padding: 15px; border-radius: 8px; box-shadow: 0 2px 5px rgba(0,0,0,0.1);">
            <h3 style="color: #2c5282; margin-top: 0; border-bottom: 2px solid #e2e8f0; padding-bottom: 10px;">Curso:</h3>
            <p style="margin: 8px 0; font-size: 16px;">Visualización de toma de decisiones</p>
            <p style="margin: 8px 0; font-size: 16px;">(PREICA2501B020125)</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div style="background-color: #f8f9fa; padding: 15px; border-radius: 8px; box-shadow: 0 2px 5px rgba(0,0,0,0.1); margin-top: 15px;">
            <h3 style="color: #2c5282; margin-top: 0; border-bottom: 2px solid #e2e8f0; padding-bottom: 10px;">Programa:</h3>
            <p style="margin: 8px 0; font-size: 16px;">Ingeniería De Software y Datos</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Centrar la información de la universidad
    st.markdown("<hr style='margin: 30px 0'>", unsafe_allow_html=True)
    
    st.markdown("""
    <div style="text-align: center; background-color: #f0f4f8; padding: 20px; border-radius: 8px; box-shadow: 0 4px 8px rgba(0,0,0,0.1); margin: 0 auto; max-width: 600px;">
        <h2 style="color: #2c5282; margin-bottom: 10px; font-weight: 600;">Institución Universitaria Digital de Antioquia</h2>
        <p style="font-size: 18px; color: #4a5568; margin-bottom: 0;">2025</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Introducción
    st.header("Introducción")
    st.write("""
    En la actualidad, el análisis de datos se ha convertido en una actividad esencial para la toma de decisiones en diversos contextos. 
    Sin embargo, interpretar correctamente los datos no solo depende de su calidad, sino también de la manera en que se visualizan. 
    Las herramientas de visualización de datos permiten transformar grandes volúmenes de información en gráficos comprensibles 
    que facilitan la identificación de patrones, tendencias y relaciones clave. En esta evidencia se analizarán diferentes herramientas 
    de visualización, evaluando sus características, fortalezas y limitaciones, para luego seleccionar la más adecuada que permita 
    abordar un caso de estudio con datos simulados.
    """)
    
    # Objetivos
    st.header("Objetivos")
    st.markdown("""
    - Investigar y comparar al menos tres herramientas populares de visualización de datos.
    - Seleccionar la herramienta más adecuada para analizar un conjunto de datos simulados con diferentes tipos de variables.
    - Justificar la elección de la herramienta considerando criterios técnicos y prácticos.
    - Crear al menos dos visualizaciones diferentes que den respuesta a los objetivos del análisis.
    - Documentar el proceso de configuración y ejecución mediante un informe y un video explicativo.
    """)
    
    # Investigación de herramientas
    st.header("Investigación de herramientas de visualización de datos")
    st.write("""
    A continuación, se presenta una comparativa de tres herramientas populares de visualización de datos: 
    Tableau, Streamlit y Python (con las bibliotecas Seaborn y Plotly). Se analizan sus características principales, 
    ventajas, desventajas y casos de uso ideales.
    """)
    
    # Tableau
    with st.expander("Herramienta 1: Tableau", expanded=True):
        st.subheader("Descripción:")
        st.write("""
        Tableau es una herramienta de visualización de datos ampliamente utilizada por empresas y profesionales del análisis de datos. 
        Permite crear dashboards interactivos y representaciones visuales de datos de forma intuitiva y sin necesidad de programar.
        """)
        
        st.subheader("Ventajas:")
        st.markdown("""
        - Interfaz gráfica amigable y de fácil uso.
        - Gran variedad de gráficos y visualizaciones avanzadas.
        - Capacidad para conectar con múltiples fuentes de datos (Excel, SQL, Google Sheets, entre otras).
        - Actualización en tiempo real de dashboards con datos conectados en vivo.
        - Amplia comunidad de usuarios y recursos de aprendizaje.
        """)
        
        st.subheader("Desventajas:")
        st.markdown("""
        - Es una herramienta de pago (con versión gratuita limitada llamada Tableau Public).
        - Puede tener una curva de aprendizaje empinada para visualizaciones complejas.
        - Algunas funciones avanzadas requieren conocimientos más técnicos.
        """)
        
        st.subheader("Casos de uso ideales:")
        st.markdown("""
        - Visualización de datos empresariales y de mercado.
        - Análisis de rendimiento y métricas en tiempo real.
        - Presentaciones profesionales e interactivas para juntas directivas o clientes.
        """)
    
    # Streamlit
    with st.expander("Herramienta 2: Streamlit", expanded=True):
        st.subheader("Descripción:")
        st.write("""
        Streamlit es una herramienta de código abierto que permite crear aplicaciones web interactivas para visualización de datos 
        utilizando Python. Es especialmente útil para científicos de datos y desarrolladores que quieren compartir sus análisis de forma 
        interactiva sin necesidad de conocimientos avanzados en desarrollo web.
        """)
        
        st.subheader("Ventajas:")
        st.markdown("""
        - Totalmente gratuito y de código abierto.
        - Sintaxis simple y directa en Python.
        - Permite crear aplicaciones web interactivas con pocas líneas de código.
        - Integración perfecta con librerías populares de ciencia de datos como Pandas, NumPy, Matplotlib, Plotly, etc.
        - Despliegue sencillo en la nube a través de Streamlit Cloud.
        """)
        
        st.subheader("Desventajas:")
        st.markdown("""
        - Requiere conocimientos básicos de programación en Python.
        - Menos opciones de personalización visual que herramientas comerciales.
        - Puede tener limitaciones de rendimiento con conjuntos de datos muy grandes.
        """)
        
        st.subheader("Casos de uso ideales:")
        st.markdown("""
        - Prototipos rápidos de dashboards y aplicaciones de datos.
        - Proyectos académicos y de investigación.
        - Compartir análisis de datos de forma interactiva con equipos o clientes.
        """)
    
    # Python
    with st.expander("Herramienta 3: Python (bibliotecas Seaborn y Plotly)", expanded=True):
        st.subheader("Descripción:")
        st.write("""
        Python es un lenguaje de programación muy utilizado en ciencia de datos, y junto con bibliotecas como Seaborn y Plotly, 
        permite crear visualizaciones estáticas y dinámicas altamente personalizadas.
        """)
        
        st.subheader("Ventajas:")
        st.markdown("""
        - Total flexibilidad en el diseño y personalización de gráficos.
        - Ideal para análisis estadístico profundo y visualización exploratoria.
        - Integración con librerías de análisis de datos como Pandas y NumPy.
        - Plotly permite gráficos interactivos que pueden integrarse en páginas web o notebooks.
        """)
        
        st.subheader("Desventajas:")
        st.markdown("""
        - Requiere conocimientos de programación en Python.
        - No tiene una interfaz gráfica visual (todo se hace por código).
        - Puede consumir más tiempo para tareas simples si se compara con herramientas visuales como Streamlit o Tableau.
        """)
        
        st.subheader("Casos de uso ideales:")
        st.markdown("""
        - Análisis exploratorio en ciencia de datos.
        - Proyectos de investigación o académicos con requerimientos personalizados.
        - Integración de visualizaciones en aplicaciones web o dashboards personalizados.
        """)
    
    # Justificación
    st.header("Justificación de la selección de la herramienta")
    st.write("""
    Para llevar a cabo el análisis de tendencias turísticas en Europa 2023, elegimos Streamlit como herramienta principal, 
    ya que consideramos que se ajustaba muy bien a los distintos objetivos del proyecto. A continuación, explicamos por qué 
    fue la opción más adecuada teniendo en cuenta varios factores clave:
    """)
    
    st.subheader("Complejidad de los datos:")
    st.write("""
    Aunque los datos estaban organizados en Excel, incluían distintos tipos de variables: numéricas, categóricas, fechas y 
    datos geográficos. Streamlit nos permitió integrar toda esa información de forma ordenada, facilitando tanto la limpieza 
    como el análisis y la visualización, sin necesidad de recurrir a herramientas adicionales.
    """)
    
    st.subheader("Tipo de visualización requerida:")
    st.write("""
    Cada objetivo del proyecto requería un tipo específico de gráfico. Streamlit, junto con bibliotecas como Plotly, 
    ofrece una variedad amplia y personalizable de visualizaciones, lo cual nos permitió:
    """)
    st.markdown("""
    - Usar gráficos de barras para los patrones estacionales y la duración promedio de las estancias.
    - Aplicar barras horizontales para identificar los destinos más visitados.
    - Utilizar boxplots para analizar tanto el gasto diario por tipo de alojamiento como la satisfacción del cliente por país.
    - Crear un mapa interactivo para representar la distribución geográfica de los viajes.
    """)
    st.write("""
    Esto nos dio flexibilidad para responder a cada pregunta planteada en el estudio con la visualización más adecuada.
    """)
    
    st.subheader("Facilidad de uso:")
    st.write("""
    Si bien el equipo contaba con cierta experiencia previa en herramientas de visualización, Streamlit nos ofreció una 
    plataforma muy intuitiva que nos permitió trabajar de forma más ágil. Su interfaz facilita tanto el modelado de datos 
    como la construcción de dashboards interactivos, lo que hizo más eficiente la colaboración entre todos los miembros.
    """)
    
    st.subheader("Disponibilidad de la herramienta:")
    st.write("""
    Streamlit es completamente gratuito y de código abierto, lo que fue ideal para los requerimientos del proyecto. Además, 
    al ser una herramienta muy utilizada tanto en entornos académicos como profesionales, nos pareció una excelente oportunidad 
    para seguir fortaleciendo una habilidad útil para nuestro desarrollo futuro.
    """)
    
    # Tipo de visualizaciones
    st.header("Tipo de visualizaciones")
    st.markdown("""
    - Patrones estacionales de viaje.
    - Destinos más populares.
    - Relación entre tipo de alojamiento y gasto diario.
    - Satisfacción del cliente (valoraciones) por país y ciudad.
    - Duración promedio de estancia por destino.
    - Distribución geográfica de los viajes.
    """)
    
    # Conclusión
    st.header("Conclusión")
    st.write("""
    A lo largo de este trabajo pudimos analizar diferentes aspectos clave del turismo en Europa durante el año 2023, 
    utilizando Streamlit como herramienta principal para visualizar y explorar los datos. Gracias a las visualizaciones 
    desarrolladas, fue posible identificar patrones estacionales de viaje, los destinos más visitados, diferencias en el 
    gasto según el tipo de alojamiento, niveles de satisfacción por país, y la duración promedio de las estancias, entre 
    otros insights relevantes.
    
    El uso de Streamlit nos permitió trabajar de manera eficiente y colaborativa, integrando distintos tipos de variables 
    en una sola plataforma visual e interactiva. Esto facilitó la interpretación de la información y nos ayudó a generar 
    conclusiones basadas en datos, lo que sería de gran valor para la toma de decisiones en una agencia de turismo real.
    """)
    
    # Referencias
    st.header("Referencias Bibliográficas")
    st.markdown("""
    - Streamlit. (s/f). Streamlit.io. Recuperado el 27 de mayo de 2025, de https://streamlit.io/
    - (S/f). Tableau.com. Recuperado el 27 de mayo de 2025, de https://www.tableau.com/es-mx/why-tableau
    - López, J. (2024, mayo 2). Main differences between matplotlib, seaborn, and plotly. Datons. https://datons.ai/main-differences-between-matplotlib-seaborn-and-plotly/
    """)
