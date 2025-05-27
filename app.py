import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime
import folium
from streamlit_folium import folium_static
import calendar

# Importar módulos personalizados
from caso_estudio import mostrar_caso_estudio

# Configuración de la página
st.set_page_config(
    page_title="Análisis de Tendencias Turísticas en Europa 2023",
    page_icon="✈️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Personalizar el diseño con CSS
st.markdown("""
<style>
    .main {background-color: #f8f9fa;}
    .stTabs [data-baseweb="tab-list"] {gap: 24px;}
    .stTabs [data-baseweb="tab"] {background-color: #e6f2ff; border-radius: 4px; padding: 10px 20px;}
    .stTabs [aria-selected="true"] {background-color: #4a86e8; color: white;}
    h1 {color: #1a365d; font-weight: 800; margin-bottom: 0.5em;}
    h2 {color: #2a4365; font-weight: 700;}
    h3 {color: #2c5282; font-weight: 600;}
    .stMarkdown {line-height: 1.8;}
    div.block-container {padding-top: 2rem;}
    .insight-card {
        background-color: white;
        border-radius: 8px;
        padding: 20px;
        margin-bottom: 20px;
        border-left: 5px solid #4a86e8;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    .metric-container {
        background-color: white;
        border-radius: 8px;
        padding: 15px;
        margin: 10px 0;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
    }
    .footer {
        background-color: #f8f9fa;
        padding: 15px;
        border-radius: 8px;
        margin-top: 30px;
        border-top: 2px solid #e2e8f0;
    }
</style>
""", unsafe_allow_html=True)

# Función para cargar los datos
@st.cache_data
def load_data():
    df = pd.read_csv("data/DOC03_Datos_U2_IDSD_VIS_TOM_DEC_542_CE.csv")
    df['fecha'] = pd.to_datetime(df['fecha'])
    df['mes'] = df['fecha'].dt.month
    df['mes_nombre'] = df['fecha'].dt.month_name()
    return df

# Cargar los datos
df = load_data()

# Título y descripción
st.title("📊 Análisis de Tendencias Turísticas en Europa 2023")

st.markdown("""
<div style="background-color: white; padding: 20px; border-radius: 10px; box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);">
    <h3 style="color: #2c5282; margin-top: 0;">Desarrollado por: <span style="color: #4a86e8; font-weight: bold;"> Duván, Daniel y Angelo</span></h3>
    <p style="font-size: 16px; line-height: 1.6;">
        Esta aplicación interactiva analiza los patrones de viaje en Europa durante 2023 para identificar tendencias clave
        que pueden mejorar las ofertas y estrategias de marketing de una agencia de turismo. Utiliza los filtros a continuación
        para personalizar el análisis según tus necesidades específicas.
    </p>
</div>
""", unsafe_allow_html=True)

# Crear dos columnas para los filtros con un diseño mejorado
st.markdown("""<div style="margin: 30px 0 20px 0;"><hr style='height:2px;border-width:0;color:#4a86e8;background-color:#4a86e8'></div>""", unsafe_allow_html=True)
st.markdown("""<h2 style="color: #2a4365; display: flex; align-items: center; gap: 10px;"><span style="font-size: 24px;">🔍</span> Filtros de análisis</h2>""", unsafe_allow_html=True)
col1, col2, col3 = st.columns(3)

with col1:
    paises_seleccionados = st.multiselect(
        "Seleccionar países",
        options=df['pais'].unique(),
        default=df['pais'].unique()
    )

with col2:
    alojamientos_seleccionados = st.multiselect(
        "Seleccionar tipos de alojamiento",
        options=df['tipo_alojamiento'].unique(),
        default=df['tipo_alojamiento'].unique()
    )

with col3:
    motivos_seleccionados = st.multiselect(
        "Seleccionar motivos de viaje",
        options=df['motivo_viaje'].unique(),
        default=df['motivo_viaje'].unique()
    )

# Filtrar los datos según las selecciones
df_filtrado = df[
    df['pais'].isin(paises_seleccionados) &
    df['tipo_alojamiento'].isin(alojamientos_seleccionados) &
    df['motivo_viaje'].isin(motivos_seleccionados)
]

# Mostrar número de viajes después de filtrar con un diseño mejorado
st.markdown(f"""
<div class="metric-container">
    <h3 style="margin:0; color:#2c5282; display: flex; align-items: center; gap: 8px;">
        <span style="font-size: 24px;">📈</span> Datos analizados
    </h3>
    <div style="display: flex; align-items: center; margin-top: 10px;">
        <div style="background-color: #4a86e8; color: white; font-weight: bold; padding: 8px 16px; border-radius: 20px; font-size: 18px;">
            {len(df_filtrado)}
        </div>
        <p style="margin-left: 10px; font-size: 16px; color: #4a5568;">viajes analizados</p>
    </div>
</div>
""", unsafe_allow_html=True)

# Dividir la pantalla en pestañas con un diseño mejorado
st.markdown("""<div style="margin: 30px 0 20px 0;"><hr style='height:2px;border-width:0;color:#4a86e8;background-color:#4a86e8'></div>""", unsafe_allow_html=True)
st.markdown("""<h2 style="color: #2a4365; margin-bottom: 20px;">Análisis interactivo</h2>""", unsafe_allow_html=True)
tab1, tab2, tab3, tab4 = st.tabs(["📚 Caso de Estudio", "🗓️ Patrones y Destinos", "🏨 Alojamiento y Satisfacción", "🗺️ Duración y Distribución"])

with tab1:
    # Mostrar el caso de estudio como primera pestaña
    mostrar_caso_estudio()

with tab2:
    # Crear dos columnas para los gráficos
    col1, col2 = st.columns(2)

    with col1:
        # 1. Patrones estacionales de viaje
        st.subheader("Patrones estacionales de viaje")

        # Ordenar los meses cronológicamente
        meses_orden = {
            'January': 1, 'February': 2, 'March': 3, 'April': 4,
            'May': 5, 'June': 6, 'July': 7, 'August': 8,
            'September': 9, 'October': 10, 'November': 11, 'December': 12
        }

        # Contar viajes por mes y ordenar
        viajes_por_mes = df_filtrado['mes_nombre'].value_counts().reset_index()
        viajes_por_mes.columns = ['Mes', 'Número de viajes']
        viajes_por_mes['orden_mes'] = viajes_por_mes['Mes'].map(meses_orden)
        viajes_por_mes = viajes_por_mes.sort_values('orden_mes')

        # Crear gráfico de barras con nuevos colores
        fig_meses = px.bar(
            viajes_por_mes,
            x='Mes',
            y='Número de viajes',
            color='Número de viajes',
            color_continuous_scale='Blues',
            title='Número de viajes por mes'
        )
        fig_meses.update_layout(xaxis_title='Mes', yaxis_title='Número de viajes')
        st.plotly_chart(fig_meses, use_container_width=True)

        # Análisis de patrones estacionales
        max_mes = viajes_por_mes.loc[viajes_por_mes['Número de viajes'].idxmax()]
        min_mes = viajes_por_mes.loc[viajes_por_mes['Número de viajes'].idxmin()]

        st.markdown(f"""
        **Insights:**
        - La temporada alta es en **{max_mes['Mes']}** con **{max_mes['Número de viajes']}** viajes.
        - La temporada baja es en **{min_mes['Mes']}** con **{min_mes['Número de viajes']}** viajes.
        """)

    with col2:
        # 2. Destinos más populares
        st.subheader("Destinos más populares")

        # Contar viajes por ciudad y obtener top 10
        top_ciudades = df_filtrado['ciudad'].value_counts().nlargest(10).reset_index()
        top_ciudades.columns = ['Ciudad', 'Número de viajes']

        # Crear gráfico de barras horizontales con nuevos colores
        fig_ciudades = px.bar(
            top_ciudades,
            y='Ciudad',
            x='Número de viajes',
            color='Número de viajes',
            color_continuous_scale='Reds',
            orientation='h',
            title='Top 10 ciudades más visitadas'
        )
        fig_ciudades.update_layout(yaxis_title='Ciudad', xaxis_title='Número de viajes')
        st.plotly_chart(fig_ciudades, use_container_width=True)

        # Análisis de destinos populares
        top_ciudad = top_ciudades.iloc[0]

        st.markdown(f"""
        **Insights:**
        - **{top_ciudad['Ciudad']}** es la ciudad más visitada con **{top_ciudad['Número de viajes']}** viajes.
        - Las 3 ciudades más populares representan el **{round(top_ciudades.iloc[:3]['Número de viajes'].sum() / df_filtrado.shape[0] * 100, 1)}%** del total de viajes.
        """)

with tab3:
    # Crear dos columnas para los gráficos
    col1, col2 = st.columns(2)

    with col1:
        # 3. Relación entre tipo de alojamiento y gasto diario
        st.subheader("Relación entre tipo de alojamiento y gasto diario")

        # Crear diagrama de caja con nuevos colores
        fig_alojamiento = px.box(
            df_filtrado,
            x='tipo_alojamiento',
            y='gasto_diario',
            color='tipo_alojamiento',
            color_discrete_sequence=px.colors.qualitative.Pastel,
            title='Gasto diario por tipo de alojamiento'
        )
        fig_alojamiento.update_layout(xaxis_title='Tipo de alojamiento', yaxis_title='Gasto diario (€)')
        st.plotly_chart(fig_alojamiento, use_container_width=True)

        # Análisis de gasto por tipo de alojamiento
        gasto_promedio = df_filtrado.groupby('tipo_alojamiento')['gasto_diario'].mean().reset_index()
        gasto_promedio = gasto_promedio.sort_values('gasto_diario', ascending=False)

        st.markdown(f"""
        **Insights:**
        - Los alojamientos tipo **{gasto_promedio.iloc[0]['tipo_alojamiento']}** tienen el mayor gasto diario promedio (**{round(gasto_promedio.iloc[0]['gasto_diario'], 2)}€**).
        - Los alojamientos tipo **{gasto_promedio.iloc[-1]['tipo_alojamiento']}** tienen el menor gasto diario promedio (**{round(gasto_promedio.iloc[-1]['gasto_diario'], 2)}€**).
        """)

    with col2:
        # 4. Satisfacción del cliente por país
        st.subheader("Satisfacción del cliente por país")

        # Crear diagrama de caja con nuevos colores
        fig_valoracion = px.box(
            df_filtrado,
            x='pais',
            y='valoracion',
            color='pais',
            color_discrete_sequence=px.colors.qualitative.Bold,
            title='Valoración por país (1-5)'
        )
        fig_valoracion.update_layout(xaxis_title='País', yaxis_title='Valoración')
        st.plotly_chart(fig_valoracion, use_container_width=True)

        # Análisis de valoración por país
        valoracion_promedio = df_filtrado.groupby('pais')['valoracion'].mean().reset_index()
        valoracion_promedio = valoracion_promedio.sort_values('valoracion', ascending=False)

        st.markdown(f"""
        **Insights:**
        - **{valoracion_promedio.iloc[0]['pais']}** tiene la valoración promedio más alta (**{round(valoracion_promedio.iloc[0]['valoracion'], 2)}** de 5).
        - **{valoracion_promedio.iloc[-1]['pais']}** tiene la valoración promedio más baja (**{round(valoracion_promedio.iloc[-1]['valoracion'], 2)}** de 5).
        """)

with tab4:
    # Crear dos columnas para los gráficos
    col1, col2 = st.columns(2)

    with col1:
        # 5. Duración promedio de estancia por destino
        st.subheader("Duración promedio de estancia por destino")

        # Calcular duración promedio por ciudad
        duracion_promedio = df_filtrado.groupby('ciudad')['duracion_estancia'].mean().reset_index()
        duracion_promedio = duracion_promedio.sort_values('duracion_estancia', ascending=False).head(10)
        duracion_promedio.columns = ['Ciudad', 'Duración promedio (días)']

        # Crear gráfico de barras con nuevos colores
        fig_duracion = px.bar(
            duracion_promedio,
            x='Ciudad',
            y='Duración promedio (días)',
            color='Duración promedio (días)',
            color_continuous_scale='Greens',
            title='Top 10 ciudades con mayor duración de estancia'
        )
        fig_duracion.update_layout(xaxis_title='Ciudad', yaxis_title='Duración promedio (días)')
        st.plotly_chart(fig_duracion, use_container_width=True)

        # Análisis de duración de estancia
        top_duracion = duracion_promedio.iloc[0]

        st.markdown(f"""
        **Insights:**
        - **{top_duracion['Ciudad']}** tiene la estancia promedio más larga (**{round(top_duracion['Duración promedio (días)'], 1)}** días).
        - La duración promedio general de estancia es de **{round(df_filtrado['duracion_estancia'].mean(), 1)}** días.
        """)

    with col2:
        # 6. Distribución geográfica de los viajes
        st.subheader("Distribución geográfica de los viajes")

        # Crear mapa
        m = folium.Map(location=[48.8566, 2.3522], zoom_start=4)

        # Diccionario de colores por país
        colores_paises = {
            'España': 'red',
            'Francia': 'blue',
            'Italia': 'green',
            'Alemania': 'purple',
            'Reino Unido': 'orange'
        }

        # Añadir marcadores al mapa
        for idx, row in df_filtrado.iterrows():
            folium.CircleMarker(
                location=[row['latitud'], row['longitud']],
                radius=row['duracion_estancia'] / 3,  # Tamaño proporcional a la duración
                color=colores_paises.get(row['pais'], 'gray'),
                fill=True,
                fill_color=colores_paises.get(row['pais'], 'gray'),
                fill_opacity=0.7,
                popup=f"""
                <b>{row['ciudad']}, {row['pais']}</b><br>
                Fecha: {row['fecha'].strftime('%d-%m-%Y')}<br>
                Alojamiento: {row['tipo_alojamiento']}<br>
                Duración: {row['duracion_estancia']} días<br>
                Gasto diario: {row['gasto_diario']}€<br>
                Valoración: {row['valoracion']}/5<br>
                Motivo: {row['motivo_viaje']}
                """
            ).add_to(m)

        # Añadir leyenda
        legend_html = """
        <div style="position: fixed; bottom: 50px; left: 50px; z-index: 1000; background-color: white; padding: 10px; border: 1px solid grey; border-radius: 5px;">
        <p><b>Países:</b></p>
        """

        for pais, color in colores_paises.items():
            legend_html += f"""
            <p><i class="fa fa-circle" style="color:{color}"></i> {pais}</p>
            """

        legend_html += """
        <p><b>Tamaño:</b> Duración de la estancia</p>
        </div>
        """

        m.get_root().html.add_child(folium.Element(legend_html))

        # Mostrar mapa
        folium_static(m, width=700, height=500)

        st.markdown("""
        **Insights del mapa:**
        - Los círculos más grandes representan estancias más largas.
        - Cada color representa un país diferente.
        - Haz clic en un punto para ver detalles del viaje.
        """)

# Ya no es necesario este bloque porque el caso de estudio ahora es la primera pestaña (tab1)

# Añadir sección de conclusiones con mejor diseño
st.markdown("""<div style="margin: 40px 0 20px 0;"><hr style='height:2px;border-width:0;color:#4a86e8;background-color:#4a86e8'></div>""", unsafe_allow_html=True)
st.markdown("""<h1 style="color: #1a365d; display: flex; align-items: center; gap: 10px; margin-bottom: 20px;"><span style="font-size: 32px;">🎯</span> Conclusiones e Insights Clave</h1>""", unsafe_allow_html=True)

# Calcular algunas métricas para las conclusiones
pais_mas_visitado = df_filtrado['pais'].value_counts().idxmax()
ciudad_mas_visitada = df_filtrado['ciudad'].value_counts().idxmax()
mes_mas_popular = df_filtrado['mes_nombre'].value_counts().idxmax()
alojamiento_mas_comun = df_filtrado['tipo_alojamiento'].value_counts().idxmax()
motivo_principal = df_filtrado['motivo_viaje'].value_counts().idxmax()
gasto_promedio = df_filtrado['gasto_diario'].mean()
duracion_promedio = df_filtrado['duracion_estancia'].mean()

# Introducción a las conclusiones
st.markdown("""
<div class="insight-card" style="margin-bottom: 30px;">
    <p style="font-size: 16px; line-height: 1.8;">
        Nuestro análisis exhaustivo de las tendencias turísticas en Europa durante 2023 ha revelado patrones significativos 
        que pueden transformar las estrategias de marketing y optimizar la oferta turística.
    </p>
</div>
""", unsafe_allow_html=True)

# Destinos estratégicos
st.markdown(f"""
<div class="insight-card" style="border-left-color: #e53e3e;">
    <h3 style="color: #c53030; display: flex; align-items: center; gap: 8px; margin-top: 0;">
        <span style="font-size: 24px;">📍</span> Destinos Estratégicos
    </h3>
    <p style="font-size: 16px; line-height: 1.8;">
        <span style="font-weight: bold; color: #2d3748;">{pais_mas_visitado}</span> lidera como el destino más popular, 
        con <span style="font-weight: bold; color: #2d3748;">{ciudad_mas_visitada}</span> atrayendo el mayor número de visitantes. 
        Recomendamos enfocar campañas promocionales en estos destinos de alta demanda mientras se desarrollan paquetes 
        especiales para destinos emergentes.
    </p>
</div>
""", unsafe_allow_html=True)

# Patrones temporales
st.markdown(f"""
<div class="insight-card" style="border-left-color: #3182ce;">
    <h3 style="color: #2b6cb0; display: flex; align-items: center; gap: 8px; margin-top: 0;">
        <span style="font-size: 24px;">📅</span> Patrones Temporales
    </h3>
    <p style="font-size: 16px; line-height: 1.8;">
        <span style="font-weight: bold; color: #2d3748;">{mes_mas_popular}</span> muestra el pico de actividad turística. 
        Sugerimos implementar precios dinámicos y ofertas especiales para temporadas bajas para optimizar 
        la ocupación durante todo el año.
    </p>
</div>
""", unsafe_allow_html=True)

# Preferencias de alojamiento
st.markdown(f"""
<div class="insight-card" style="border-left-color: #38a169;">
    <h3 style="color: #2f855a; display: flex; align-items: center; gap: 8px; margin-top: 0;">
        <span style="font-size: 24px;">🏠</span> Preferencias de Alojamiento
    </h3>
    <p style="font-size: 16px; line-height: 1.8;">
        Los viajeros prefieren mayoritariamente <span style="font-weight: bold; color: #2d3748;">{alojamiento_mas_comun.lower()}</span>, 
        lo que indica una oportunidad para desarrollar alianzas estratégicas con estos proveedores y crear paquetes exclusivos.
    </p>
</div>
""", unsafe_allow_html=True)

# Análisis económico
st.markdown(f"""
<div class="insight-card" style="border-left-color: #d69e2e;">
    <h3 style="color: #b7791f; display: flex; align-items: center; gap: 8px; margin-top: 0;">
        <span style="font-size: 24px;">💰</span> Análisis Económico
    </h3>
    <p style="font-size: 16px; line-height: 1.8;">
        Con un gasto diario promedio de <span style="font-weight: bold; color: #2d3748;">{round(gasto_promedio, 2)}€</span> 
        y estancias que promedian <span style="font-weight: bold; color: #2d3748;">{round(duracion_promedio, 1)} días</span>, 
        identificamos un potencial para desarrollar paquetes de valor agregado que incrementen tanto la duración como el gasto.
    </p>
</div>
""", unsafe_allow_html=True)

# Motivaciones de viaje
st.markdown(f"""
<div class="insight-card" style="border-left-color: #805ad5;">
    <h3 style="color: #6b46c1; display: flex; align-items: center; gap: 8px; margin-top: 0;">
        <span style="font-size: 24px;">🔍</span> Motivaciones de Viaje
    </h3>
    <p style="font-size: 16px; line-height: 1.8;">
        El motivo principal de viaje es <span style="font-weight: bold; color: #2d3748;">{motivo_principal.lower()}</span>, 
        lo que sugiere que las campañas de marketing deberían enfatizar experiencias relacionadas con esta motivación 
        para maximizar su impacto.
    </p>
</div>
""", unsafe_allow_html=True)

# Se ha eliminado el pie de página