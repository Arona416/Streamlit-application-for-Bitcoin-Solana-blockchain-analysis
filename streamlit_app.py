import streamlit as st
from utils.language import TRANSLATIONS, DEFAULT_LANG, get_text

# Configuration de la page
st.set_page_config(page_title="Blockchain Dashboard", page_icon="💱", layout="wide")

# Initialisation de la langue
if "lang" not in st.session_state:
    st.session_state["lang"] = DEFAULT_LANG

# Sélecteur de langue dynamique
langue_selectionnee = st.sidebar.selectbox(
    "Language / Langue / язык",
    options=["FR", "EN", "RU"],
    format_func=lambda x: TRANSLATIONS[x]["lang_name"],
    key="lang"
)

lang = st.session_state["lang"]

# Titre et texte d'accueil
st.title(get_text("welcome_title", lang))
st.write(get_text("welcome_text", lang))

# Sommaire dynamique en Markdown
st.markdown(f"""
- 📈 {get_text('menu_bitcoin', lang)}
- ⚡ {get_text('menu_solana', lang)}
- 🔍 {get_text('menu_comparaison', lang)}
- 🎓 {get_text('menu_education', lang)}
""")
