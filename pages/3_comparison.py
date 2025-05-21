import streamlit as st
from utils.language import TRANSLATIONS
from api import coingecko_api

# Configuration de la langue et de la page
if 'lang' not in st.session_state:
    st.session_state.lang = 'FR'
lang = st.session_state.lang
st.set_page_config(page_title=TRANSLATIONS[lang]['page_title_comparison'], page_icon="🔗")

# Sélecteur de langue dans la barre latérale
lang_options = {"Français": "FR", "English": "EN", "Русский": "RU"}
choice = st.sidebar.selectbox(TRANSLATIONS[lang]['language_label'], 
                              options=list(lang_options.keys()), 
                              index=list(lang_options.values()).index(lang))
st.session_state.lang = lang_options[choice]
lang = st.session_state.lang

# Titre de la page Comparaison
st.title(TRANSLATIONS[lang]['comparison_title'])

# Récupération de l'historique des prix (30 derniers jours) pour BTC et SOL via CoinGecko
btc_history = coingecko_api.get_price_history('bitcoin', days=30)
sol_history = coingecko_api.get_price_history('solana', days=30)

# Génération du graphique de comparaison des prix BTC vs SOL
from utils import visuals
fig = visuals.make_price_comparison_chart(btc_history, sol_history, title=TRANSLATIONS[lang]['comp_chart_title'])
st.plotly_chart(fig, use_container_width=True)
