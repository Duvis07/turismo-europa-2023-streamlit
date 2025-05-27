import streamlit as st

# Constantes para textos repetidos
DESCRIPCION = "Descripción:"
VENTAJAS = "Ventajas:"
DESVENTAJAS = "Desventajas:"
CASOSUSO = "Casos de uso ideales:"
VER_DETALLES = "Ver detalles"

def mostrar_caso_estudio():
    st.markdown("<h1 style='font-size: 36px; color: #1a365d;'>Caso de estudio: análisis de los diferentes tipos de datos</h1>", unsafe_allow_html=True)
    

    
    # Introducción
    st.markdown("<h2 style='font-size: 32px; color: #1a365d;'>Introducción</h2>", unsafe_allow_html=True)
    st.write("""
    En la actualidad, el análisis de datos se ha convertido en una actividad esencial para la toma de decisiones en diversos contextos. 
    Sin embargo, interpretar correctamente los datos no solo depende de su calidad, sino también de la manera en que se visualizan. 
    Las herramientas de visualización de datos permiten transformar grandes volúmenes de información en gráficos comprensibles 
    que facilitan la identificación de patrones, tendencias y relaciones clave. En esta evidencia se analizarán diferentes herramientas 
    de visualización, evaluando sus características, fortalezas y limitaciones, para luego seleccionar la más adecuada que permita 
    abordar un caso de estudio con datos simulados.
    """)
    
    # Objetivos
    st.markdown("<h2 style='font-size: 32px; color: #1a365d;'>Objetivos</h2>", unsafe_allow_html=True)
    st.markdown("""
    - Investigar y comparar al menos tres herramientas populares de visualización de datos.
    - Seleccionar la herramienta más adecuada para analizar un conjunto de datos simulados con diferentes tipos de variables.
    - Justificar la elección de la herramienta considerando criterios técnicos y prácticos.
    - Crear al menos dos visualizaciones diferentes que den respuesta a los objetivos del análisis.
    - Documentar el proceso de configuración y ejecución mediante un informe y un video explicativo.
    """)
    
    # Investigación de herramientas
    st.markdown("<h2 style='font-size: 32px; color: #1a365d;'>Investigación de herramientas de visualización de datos</h2>", unsafe_allow_html=True)
    st.write("""
    A continuación, se presenta una comparativa de tres herramientas populares de visualización de datos: 
    Tableau, Streamlit y Python (con las bibliotecas Seaborn y Plotly). Se analizan sus características principales, 
    ventajas, desventajas y casos de uso ideales.
    """)
    
    # Tableau
    st.markdown("<h2 style='font-size: 24px; color: #1a365d;'>Herramienta 1: Tableau</h2>", unsafe_allow_html=True)
    with st.expander("Ver detalles", expanded=True):
        st.subheader(DESCRIPCION)
        st.write("""
        Tableau es una herramienta de visualización de datos ampliamente utilizada por empresas y profesionales del análisis de datos. 
        Permite crear dashboards interactivos y representaciones visuales de datos de forma intuitiva y sin necesidad de programar.
        """)
        
        st.subheader(VENTAJAS)
        st.markdown("""
        - Interfaz gráfica amigable y de fácil uso.
        - Gran variedad de gráficos y visualizaciones avanzadas.
        - Capacidad para conectar con múltiples fuentes de datos (Excel, SQL, Google Sheets, entre otras).
        - Actualización en tiempo real de dashboards con datos conectados en vivo.
        - Amplia comunidad de usuarios y recursos de aprendizaje.
        """)
        
        st.subheader(DESVENTAJAS)
        st.markdown("""
        - Es una herramienta de pago (con versión gratuita limitada llamada Tableau Public).
        - Puede tener una curva de aprendizaje empinada para visualizaciones complejas.
        - Algunas funciones avanzadas requieren conocimientos más técnicos.
        """)
        
        st.subheader(CASOSUSO)
        st.markdown("""
        - Visualización de datos empresariales y de mercado.
        - Análisis de rendimiento y métricas en tiempo real.
        - Presentaciones profesionales e interactivas para juntas directivas o clientes.
        """)
    
    # Streamlit
    st.markdown("<h2 style='font-size: 24px; color: #1a365d;'>Herramienta 2: Streamlit</h2>", unsafe_allow_html=True)
    with st.expander("Ver detalles", expanded=True):
        st.subheader(DESCRIPCION)
        st.write("""
        Streamlit es una herramienta de código abierto que permite crear aplicaciones web interactivas para visualización de datos 
        utilizando Python. Es especialmente útil para científicos de datos y desarrolladores que quieren compartir sus análisis de forma 
        interactiva sin necesidad de conocimientos avanzados en desarrollo web.
        """)
        
        st.subheader(VENTAJAS)
        st.markdown("""
        - Totalmente gratuito y de código abierto.
        - Sintaxis simple y directa en Python.
        - Permite crear aplicaciones web interactivas con pocas líneas de código.
        - Integración perfecta con librerías populares de ciencia de datos como Pandas, NumPy, Matplotlib, Plotly, etc.
        - Despliegue sencillo en la nube a través de Streamlit Cloud.
        """)
        
        st.subheader(DESVENTAJAS)
        st.markdown("""
        - Requiere conocimientos básicos de programación en Python.
        - Menos opciones de personalización visual que herramientas comerciales.
        - Puede tener limitaciones de rendimiento con conjuntos de datos muy grandes.
        """)
        
        st.subheader(CASOSUSO)
        st.markdown("""
        - Prototipos rápidos de dashboards y aplicaciones de datos.
        - Proyectos académicos y de investigación.
        - Compartir análisis de datos de forma interactiva con equipos o clientes.
        """)
    
    # Python
    st.markdown("<h2 style='font-size: 24px; color: #1a365d;'>Herramienta 3: Python (bibliotecas Seaborn y Plotly)</h2>", unsafe_allow_html=True)
    with st.expander("Ver detalles", expanded=True):
        st.subheader(DESCRIPCION)
        st.write("""
        Python es un lenguaje de programación muy utilizado en ciencia de datos, y junto con bibliotecas como Seaborn y Plotly, 
        permite crear visualizaciones estáticas y dinámicas altamente personalizadas.
        """)
        
        st.subheader(VENTAJAS)
        st.markdown("""
        - Total flexibilidad en el diseño y personalización de gráficos.
        - Ideal para análisis estadístico profundo y visualización exploratoria.
        - Integración con librerías de análisis de datos como Pandas y NumPy.
        - Plotly permite gráficos interactivos que pueden integrarse en páginas web o notebooks.
        """)
        
        st.subheader(DESVENTAJAS)
        st.markdown("""
        - Requiere conocimientos de programación en Python.
        - No tiene una interfaz gráfica visual (todo se hace por código).
        - Puede consumir más tiempo para tareas simples si se compara con herramientas visuales como Streamlit o Tableau.
        """)
        
        st.subheader(CASOSUSO)
        st.markdown("""
        - Análisis exploratorio en ciencia de datos.
        - Proyectos de investigación o académicos con requerimientos personalizados.
        - Integración de visualizaciones en aplicaciones web o dashboards personalizados.
        """)
    
    # Justificación
    st.markdown("<h2 style='font-size: 32px; color: #1a365d;'>Justificación de la selección de la herramienta</h2>", unsafe_allow_html=True)
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
    st.markdown("<h2 style='font-size: 32px; color: #1a365d;'>Tipo de visualizaciones</h2>", unsafe_allow_html=True)
    st.markdown("""
    - Patrones estacionales de viaje.
    - Destinos más populares.
    - Relación entre tipo de alojamiento y gasto diario.
    - Satisfacción del cliente (valoraciones) por país y ciudad.
    - Duración promedio de estancia por destino.
    - Distribución geográfica de los viajes.
    """)
    
    # Conclusión
    st.markdown("<h2 style='font-size: 32px; color: #1a365d;'>Conclusión</h2>", unsafe_allow_html=True)
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
    st.markdown("<h2 style='font-size: 32px; color: #1a365d;'>Referencias Bibliográficas</h2>", unsafe_allow_html=True)
    st.markdown("""
    - Streamlit. (s/f). Streamlit.io. Recuperado el 27 de mayo de 2025, de https://streamlit.io/
    - (S/f). Tableau.com. Recuperado el 27 de mayo de 2025, de https://www.tableau.com/es-mx/why-tableau
    - López, J. (2024, mayo 2). Main differences between matplotlib, seaborn, and plotly. Datons. https://datons.ai/main-differences-between-matplotlib-seaborn-and-plotly/
    """)
