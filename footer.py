import streamlit as st

def mostrar_footer():
    """Muestra el pie de página de la aplicación."""
    # Añadir espacio antes del footer
    st.markdown("##")
    
    # Añadir línea divisoria
    st.markdown("---")
    
    # Crear tres columnas para el footer
    col1, col2 = st.columns([1, 1])
    
    # Columna izquierda
    with col1:
        st.text("© 2025")
        st.markdown("**Desarrollado por Daniel, Duvan y Angelo**")
    
    # Columna derecha (alineada a la derecha manualmente)
    with col2:
        # Usar markdown con espacios para alinear a la derecha
        st.markdown("<p style='text-align: right;'>Análisis de Tendencias Turísticas</p>", unsafe_allow_html=True)
        st.markdown("<p style='text-align: right;'>Europa 2023</p>", unsafe_allow_html=True)
