import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime
import folium
from streamlit_folium import folium_static
import calendar

# Constantes para evitar duplicados (corrige errores de lint)
COL_NUM_VIAJES = 'Número de viajes'
COL_DURACION_DIAS = 'Duración promedio (días)'

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
        st.markdown("<h2 style='font-size: 28px; color: #1a365d;'>Patrones estacionales de viaje</h2>", unsafe_allow_html=True)

        # Ordenar los meses cronológicamente
        meses_orden = {
            'January': 1, 'February': 2, 'March': 3, 'April': 4,
            'May': 5, 'June': 6, 'July': 7, 'August': 8,
            'September': 9, 'October': 10, 'November': 11, 'December': 12
        }

        # Contar viajes por mes y ordenar
        viajes_por_mes = df_filtrado['mes_nombre'].value_counts().reset_index()
        viajes_por_mes.columns = ['Mes', COL_NUM_VIAJES]
        viajes_por_mes['orden_mes'] = viajes_por_mes['Mes'].map(meses_orden)
        viajes_por_mes = viajes_por_mes.sort_values('orden_mes')

        # Crear gráfico de barras con nuevos colores y mayor contraste
        fig_meses = px.bar(
            viajes_por_mes,
            x='Mes',
            y=COL_NUM_VIAJES,
            color=COL_NUM_VIAJES,
            color_continuous_scale=['#E6EFF6', '#D4E6F1', '#A9CCE3', '#7FB3D5', '#5499C7', '#2980B9', '#1A5276'],
            title='Número de viajes por mes'
        )
        fig_meses.update_layout(
            xaxis_title='Mes', 
            yaxis_title=COL_NUM_VIAJES,
            coloraxis_colorbar=dict(title=COL_NUM_VIAJES),
            plot_bgcolor='white'
        )
        st.plotly_chart(fig_meses, use_container_width=True)

        # Análisis de patrones estacionales
        max_mes = viajes_por_mes.loc[viajes_por_mes[COL_NUM_VIAJES].idxmax()]
        min_mes = viajes_por_mes.loc[viajes_por_mes[COL_NUM_VIAJES].idxmin()]

        # Tarjeta de insights con diseño mejorado
        st.markdown(f"""
        <div style="background-color: #f8f9fa; border-left: 4px solid #4a86e8; padding: 15px; border-radius: 5px; margin-top: 20px; box-shadow: 0 2px 5px rgba(0,0,0,0.1);">
            <h4 style="color: #2c5282; margin-top: 0; display: flex; align-items: center; gap: 8px;">
                <span style="font-size: 20px;">📊</span> Insights Clave
            </h4>
            <ul style="margin-bottom: 0; padding-left: 20px;">
                <li style="margin-bottom: 8px;">
                    <span style="color: #4a86e8; font-weight: bold;">Temporada alta:</span> 
                    <span style="background-color: #e6f2ff; padding: 2px 6px; border-radius: 3px; font-weight: bold;">{max_mes['Mes']}</span> con 
                    <span style="background-color: #e6f2ff; padding: 2px 6px; border-radius: 3px; font-weight: bold;">{max_mes[COL_NUM_VIAJES]}</span> viajes
                </li>
                <li>
                    <span style="color: #4a86e8; font-weight: bold;">Temporada baja:</span> 
                    <span style="background-color: #e6f2ff; padding: 2px 6px; border-radius: 3px; font-weight: bold;">{min_mes['Mes']}</span> con 
                    <span style="background-color: #e6f2ff; padding: 2px 6px; border-radius: 3px; font-weight: bold;">{min_mes[COL_NUM_VIAJES]}</span> viajes
                </li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        # 2. Destinos más populares
        st.markdown("<h2 style='font-size: 28px; color: #1a365d;'>Destinos más populares</h2>", unsafe_allow_html=True)

        # Contar viajes por ciudad y obtener top 10
        top_ciudades = df_filtrado['ciudad'].value_counts().nlargest(10).reset_index()
        top_ciudades.columns = ['Ciudad', COL_NUM_VIAJES]

        # Crear gráfico de barras horizontales con nuevos colores
        fig_ciudades = px.bar(
            top_ciudades,
            y='Ciudad',
            x=COL_NUM_VIAJES,
            color=COL_NUM_VIAJES,
            color_continuous_scale='Reds',
            orientation='h',
            title='Top 10 ciudades más visitadas'
        )
        fig_ciudades.update_layout(yaxis_title='Ciudad', xaxis_title=COL_NUM_VIAJES)
        st.plotly_chart(fig_ciudades, use_container_width=True)

        # Análisis de destinos populares
        top_ciudad = top_ciudades.iloc[0]

        # Tarjeta de insights con diseño mejorado
        porcentaje_top3 = round(top_ciudades.iloc[:3][COL_NUM_VIAJES].sum() / df_filtrado.shape[0] * 100, 1)
        st.markdown(f"""
        <div style="background-color: #fdf2f2; border-left: 4px solid #e53e3e; padding: 15px; border-radius: 5px; margin-top: 20px; box-shadow: 0 2px 5px rgba(0,0,0,0.1);">
            <h4 style="color: #c53030; margin-top: 0; display: flex; align-items: center; gap: 8px;">
                <span style="font-size: 20px;">🌆</span> Insights Clave
            </h4>
            <ul style="margin-bottom: 0; padding-left: 20px;">
                <li style="margin-bottom: 8px;">
                    <span style="color: #e53e3e; font-weight: bold;">Ciudad más visitada:</span> 
                    <span style="background-color: #fff5f5; padding: 2px 6px; border-radius: 3px; font-weight: bold;">{top_ciudad['Ciudad']}</span> con 
                    <span style="background-color: #fff5f5; padding: 2px 6px; border-radius: 3px; font-weight: bold;">{top_ciudad[COL_NUM_VIAJES]}</span> viajes
                </li>
                <li>
                    <span style="color: #e53e3e; font-weight: bold;">Concentración:</span> 
                    Las 3 ciudades más populares representan el <span style="background-color: #fff5f5; padding: 2px 6px; border-radius: 3px; font-weight: bold;">{porcentaje_top3}%</span> del total de viajes
                </li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

with tab3:
    # Crear dos columnas para los gráficos
    col1, col2 = st.columns(2)

    with col1:
        # 3. Relación entre tipo de alojamiento y gasto diario
        st.markdown("<h2 style='font-size: 28px; color: #1a365d;'>Relación entre tipo de alojamiento y gasto diario</h2>", unsafe_allow_html=True)

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

        # Tarjeta de insights con diseño mejorado
        max_gasto = round(gasto_promedio.iloc[0]['gasto_diario'], 2)
        min_gasto = round(gasto_promedio.iloc[-1]['gasto_diario'], 2)
        st.markdown(f"""
        <div style="background-color: #f0fff4; border-left: 4px solid #38a169; padding: 15px; border-radius: 5px; margin-top: 20px; box-shadow: 0 2px 5px rgba(0,0,0,0.1);">
            <h4 style="color: #2f855a; margin-top: 0; display: flex; align-items: center; gap: 8px;">
                <span style="font-size: 20px;">💰</span> Insights de Gasto
            </h4>
            <ul style="margin-bottom: 0; padding-left: 20px;">
                <li style="margin-bottom: 8px;">
                    <span style="color: #38a169; font-weight: bold;">Mayor gasto:</span> 
                    Alojamientos tipo <span style="background-color: #e6ffec; padding: 2px 6px; border-radius: 3px; font-weight: bold;">{gasto_promedio.iloc[0]['tipo_alojamiento']}</span> con 
                    <span style="background-color: #e6ffec; padding: 2px 6px; border-radius: 3px; font-weight: bold;">{max_gasto}€</span> diarios
                </li>
                <li>
                    <span style="color: #38a169; font-weight: bold;">Menor gasto:</span> 
                    Alojamientos tipo <span style="background-color: #e6ffec; padding: 2px 6px; border-radius: 3px; font-weight: bold;">{gasto_promedio.iloc[-1]['tipo_alojamiento']}</span> con 
                    <span style="background-color: #e6ffec; padding: 2px 6px; border-radius: 3px; font-weight: bold;">{min_gasto}€</span> diarios
                </li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        # 4. Satisfacción del cliente por país
        st.markdown("<h2 style='font-size: 28px; color: #1a365d;'>Satisfacción del cliente por país</h2>", unsafe_allow_html=True)

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

        # Tarjeta de insights con diseño mejorado
        max_valoracion = round(valoracion_promedio.iloc[0]['valoracion'], 2)
        min_valoracion = round(valoracion_promedio.iloc[-1]['valoracion'], 2)
        st.markdown(f"""
        <div style="background-color: #ebf8ff; border-left: 4px solid #3182ce; padding: 15px; border-radius: 5px; margin-top: 20px; box-shadow: 0 2px 5px rgba(0,0,0,0.1);">
            <h4 style="color: #2b6cb0; margin-top: 0; display: flex; align-items: center; gap: 8px;">
                <span style="font-size: 20px;">⭐</span> Insights de Satisfacción
            </h4>
            <ul style="margin-bottom: 0; padding-left: 20px;">
                <li style="margin-bottom: 8px;">
                    <span style="color: #3182ce; font-weight: bold;">Mayor satisfacción:</span> 
                    <span style="background-color: #e6f6ff; padding: 2px 6px; border-radius: 3px; font-weight: bold;">{valoracion_promedio.iloc[0]['pais']}</span> con 
                    <span style="background-color: #e6f6ff; padding: 2px 6px; border-radius: 3px; font-weight: bold;">{max_valoracion}/5</span> puntos
                </li>
                <li>
                    <span style="color: #3182ce; font-weight: bold;">Menor satisfacción:</span> 
                    <span style="background-color: #e6f6ff; padding: 2px 6px; border-radius: 3px; font-weight: bold;">{valoracion_promedio.iloc[-1]['pais']}</span> con 
                    <span style="background-color: #e6f6ff; padding: 2px 6px; border-radius: 3px; font-weight: bold;">{min_valoracion}/5</span> puntos
                </li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

with tab4:
    # Crear dos columnas para los gráficos
    col1, col2 = st.columns(2)

    with col1:
        # 5. Duración promedio de estancia por destino
        st.markdown("<h2 style='font-size: 28px; color: #1a365d;'>Duración promedio de estancia por destino</h2>", unsafe_allow_html=True)

        # Calcular duración promedio por ciudad
        duracion_promedio = df_filtrado.groupby('ciudad')['duracion_estancia'].mean().reset_index()
        duracion_promedio = duracion_promedio.sort_values('duracion_estancia', ascending=False).head(10)
        duracion_promedio.columns = ['Ciudad', COL_DURACION_DIAS]

        # Crear gráfico de barras con nuevos colores
        fig_duracion = px.bar(
            duracion_promedio,
            x='Ciudad',
            y=COL_DURACION_DIAS,
            color=COL_DURACION_DIAS,
            color_continuous_scale='Greens',
            title='Top 10 ciudades con mayor duración de estancia'
        )
        fig_duracion.update_layout(xaxis_title='Ciudad', yaxis_title=COL_DURACION_DIAS)
        st.plotly_chart(fig_duracion, use_container_width=True)

        # Análisis de duración de estancia
        top_duracion = duracion_promedio.iloc[0]

        # Tarjeta de insights con diseño mejorado
        max_duracion = round(top_duracion[COL_DURACION_DIAS], 1)
        promedio_general = round(df_filtrado['duracion_estancia'].mean(), 1)
        st.markdown(f"""
        <div style="background-color: #f0fff4; border-left: 4px solid #48bb78; padding: 15px; border-radius: 5px; margin-top: 20px; box-shadow: 0 2px 5px rgba(0,0,0,0.1);">
            <h4 style="color: #2f855a; margin-top: 0; display: flex; align-items: center; gap: 8px;">
                <span style="font-size: 20px;">📅</span> Insights de Duración
            </h4>
            <ul style="margin-bottom: 0; padding-left: 20px;">
                <li style="margin-bottom: 8px;">
                    <span style="color: #48bb78; font-weight: bold;">Estancia más larga:</span> 
                    <span style="background-color: #e6ffec; padding: 2px 6px; border-radius: 3px; font-weight: bold;">{top_duracion['Ciudad']}</span> con 
                    <span style="background-color: #e6ffec; padding: 2px 6px; border-radius: 3px; font-weight: bold;">{max_duracion} días</span>
                </li>
                <li>
                    <span style="color: #48bb78; font-weight: bold;">Promedio general:</span> 
                    <span style="background-color: #e6ffec; padding: 2px 6px; border-radius: 3px; font-weight: bold;">{promedio_general} días</span> de estancia
                </li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        # 6. Distribución geográfica de los viajes
        st.markdown("<h2 style='font-size: 28px; color: #1a365d;'>Distribución geográfica de los viajes</h2>", unsafe_allow_html=True)

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

        # Tarjeta de insights con diseño mejorado
        st.markdown("""
        <div style="background-color: #faf5ff; border-left: 4px solid #805ad5; padding: 15px; border-radius: 5px; margin-top: 20px; box-shadow: 0 2px 5px rgba(0,0,0,0.1);">
            <h4 style="color: #553c9a; margin-top: 0; display: flex; align-items: center; gap: 8px;">
                <span style="font-size: 20px;">📍</span> Insights del Mapa
            </h4>
            <ul style="margin-bottom: 0; padding-left: 20px;">
                <li style="margin-bottom: 8px;">
                    <span style="color: #805ad5; font-weight: bold;">Tamaño:</span> 
                    Los círculos más grandes representan estancias más largas
                </li>
                <li style="margin-bottom: 8px;">
                    <span style="color: #805ad5; font-weight: bold;">Color:</span> 
                    Cada color representa un país diferente
                </li>
                <li>
                    <span style="color: #805ad5; font-weight: bold;">Interacción:</span> 
                    Haz clic en un punto para ver detalles del viaje
                </li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

# Se ha eliminado la sección de Conclusiones e Insights Clave

# Se ha eliminado el pie de página