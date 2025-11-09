"""
ContaX Portal - Portal Corporativo Streamlit
============================================

Portal corporativo para centralizar acesso a diferentes sistemas e ferramentas
da empresa ContaX através de uma interface unificada e moderna.

Autor: ContaX Development Team
Data: 2025
"""

import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path
import sys
import importlib.util

# Adiciona o diretório raiz ao path para importar config
BASE_DIR = Path(__file__).parent
sys.path.insert(0, str(BASE_DIR))

# Importa as configurações de URLs
try:
    from config.urls import tabs
except ImportError:
    # Fallback caso a importação falhe
    tabs = {
        "Home": "https://www.contax.com.br",
        "Portal Financeiro": "https://gdp-dashboard-60uvb3secte.streamlit.app/",
        "Chatbot": "ttps://chatbot-3ysuzjb5ovm.streamlit.app",
        "Plataforma de Extração de Documentos": "https://extraction-document-v1.streamlit.app/"
    }

# ============================================================================
# CONFIGURAÇÃO DA PÁGINA
# ============================================================================

st.set_page_config(
    page_title="ContaX Portal",
    page_icon="🏢",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ============================================================================
# CONSTANTES E CONFIGURAÇÕES
# ============================================================================

# Cores corporativas
COLOR_PRIMARY = "#0052CC"
COLOR_LIGHT_BLUE = "#F4F8FF"
COLOR_GRAY = "#F7F7F7"
COLOR_TEXT = "#333333"

# Caminho do logotipo
LOGO_PATH = BASE_DIR / "assets" / "contax_logo.png"

# Altura do iframe (ajustável)
IFRAME_HEIGHT = 800

# ============================================================================
# CSS PERSONALIZADO
# ============================================================================

def load_custom_css():
    """Carrega o CSS personalizado para o portal."""
    css = f"""
    <style>
        /* Esconder elementos padrão do Streamlit */
        #MainMenu {{visibility: hidden;}}
        footer {{visibility: hidden;}}
        header {{visibility: hidden;}}
        
        /* Estilo do cabeçalho */
        .main-header {{
            background: linear-gradient(135deg, {COLOR_PRIMARY} 0%, #003D99 100%);
            padding: 1.5rem 2rem;
            margin: -1rem -1rem 2rem -1rem;
            box-shadow: 0 2px 10px rgba(0, 82, 204, 0.2);
            display: flex;
            align-items: center;
            gap: 1.5rem;
        }}
        
        .logo-container {{
            display: flex;
            align-items: center;
            gap: 1rem;
        }}
        
        .logo-img {{
            max-height: 50px;
            width: auto;
        }}
        
        .portal-title {{
            color: white;
            font-size: 1.8rem;
            font-weight: 600;
            margin: 0;
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
        }}
        
        /* Estilo das abas */
        .stTabs [data-baseweb="tab-list"] {{
            gap: 0.5rem;
            background-color: {COLOR_GRAY};
            padding: 0.5rem;
            border-radius: 8px;
        }}
        
        .stTabs [data-baseweb="tab"] {{
            background-color: transparent;
            border-radius: 6px;
            padding: 0.75rem 1.5rem;
            font-weight: 500;
            color: {COLOR_TEXT};
            transition: all 0.3s ease;
        }}
        
        .stTabs [aria-selected="true"] {{
            background-color: {COLOR_PRIMARY};
            color: white;
        }}
        
        /* Container principal */
        .main-container {{
            background-color: {COLOR_LIGHT_BLUE};
            min-height: calc(100vh - 200px);
            padding: 2rem;
            border-radius: 10px;
        }}
        
        /* Estilo do iframe */
        .iframe-container {{
            background-color: white;
            border-radius: 8px;
            padding: 1rem;
            box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
            margin-top: 1rem;
        }}
        
        /* Rodapé */
        .footer {{
            text-align: center;
            padding: 1.5rem;
            color: {COLOR_TEXT};
            font-size: 0.9rem;
            margin-top: 2rem;
            border-top: 1px solid #E0E0E0;
        }}
        
        /* Responsividade */
        @media (max-width: 768px) {{
            .main-header {{
                padding: 1rem;
                flex-direction: column;
                text-align: center;
            }}
            
            .portal-title {{
                font-size: 1.4rem;
            }}
            
            .logo-img {{
                max-height: 40px;
            }}
        }}
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)

# ============================================================================
# FUNÇÕES AUXILIARES
# ============================================================================

def render_header():
    """Renderiza o cabeçalho com logotipo e título."""
    # Verifica se o logotipo existe
    if LOGO_PATH.exists():
        logo_html = f"""
        <div class="main-header">
            <div class="logo-container">
                <img src="data:image/png;base64,{get_logo_base64()}" class="logo-img" alt="ContaX Logo">
                <h1 class="portal-title">ContaX Portal</h1>
            </div>
        </div>
        """
    else:
        # Fallback se o logotipo não for encontrado
        logo_html = f"""
        <div class="main-header">
            <h1 class="portal-title">ContaX Portal</h1>
        </div>
        """
    
    st.markdown(logo_html, unsafe_allow_html=True)

def get_logo_base64():
    """Converte o logotipo para base64 para exibição."""
    import base64
    try:
        with open(LOGO_PATH, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    except Exception as e:
        st.error(f"Erro ao carregar logotipo: {e}")
        return ""

def render_iframe(url: str, height: int = IFRAME_HEIGHT):
    """Renderiza um iframe com a URL especificada."""
    try:
        components.iframe(
            src=url,
            height=height,
            scrolling=True
        )
    except Exception as e:
        st.error(f"Erro ao carregar a página: {e}")
        st.info(f"Tente acessar diretamente: [{url}]({url})")

def render_footer():
    """Renderiza o rodapé do portal."""
    footer_html = """
    <div class="footer">
        <p>ContaX © 2025 – Todos os direitos reservados</p>
    </div>
    """
    st.markdown(footer_html, unsafe_allow_html=True)

# ============================================================================
# APLICAÇÃO PRINCIPAL
# ============================================================================

def main():
    """Função principal da aplicação."""
    # Carrega CSS personalizado
    load_custom_css()
    
    # Renderiza cabeçalho
    render_header()
    
    # Verifica se há abas configuradas
    if not tabs:
        st.warning("⚠️ Nenhuma aba configurada. Por favor, edite o arquivo `config/urls.py`.")
        return
    
    # Cria as abas
    tab_names = list(tabs.keys())
    selected_tabs = st.tabs(tab_names)
    
    # Renderiza o conteúdo de cada aba
    for idx, (tab_name, url) in enumerate(tabs.items()):
        with selected_tabs[idx]:
            st.markdown(f"### {tab_name}")
            st.markdown(f"Carregando: `{url}`")
            
            # Container para o iframe
            with st.container():
                render_iframe(url, height=IFRAME_HEIGHT)
    
    # Renderiza rodapé
    render_footer()

# ============================================================================
# EXECUÇÃO
# ============================================================================

if __name__ == "__main__":
    main()


