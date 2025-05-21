import streamlit as st
from utils.language import TRANSLATIONS
from api import solana_api, coingecko_api

# Configuration de la langue et de la page
if 'lang' not in st.session_state:
    st.session_state.lang = 'FR'
lang = st.session_state.lang
st.set_page_config(page_title=TRANSLATIONS[lang]['page_title_solana'], page_icon="🔗")

# Sélecteur de langue dans la barre latérale
lang_options = {"Français": "FR", "English": "EN", "Русский": "RU"}
choice = st.sidebar.selectbox(TRANSLATIONS[lang]['language_label'], 
                              options=list(lang_options.keys()), 
                              index=list(lang_options.values()).index(lang))
st.session_state.lang = lang_options[choice]
lang = st.session_state.lang

# Titre de la page Solana
st.title(TRANSLATIONS[lang]['solana_title'])

# Appels API pour obtenir les données Solana actuelles
block_height = solana_api.get_solana_block_height()        # Dernier numéro de bloc Solana
samples = solana_api.get_solana_performance(samples=60)    # Échantillons de performance récents (TPS)
prices = coingecko_api.get_crypto_prices(['solana'])       # Prix du SOL en USD et variation 24h

# Vérification des données reçues
if block_height is not None and samples is not None and prices:
    sol_price = prices['solana']['usd']
    sol_change = prices['solana']['usd_24h_change']
    # Calcul du TPS moyen sur la dernière période (dernière minute)
    current_tps = None
    if len(samples) > 0:
        latest = samples[0]  # Le premier échantillon est le plus récent
        if latest.get('numTransactions') is not None and latest.get('samplePeriodSecs') is not None:
            current_tps = latest['numTransactions'] / latest['samplePeriodSecs']
    # Affichage des métriques principales de Solana
    st.metric(TRANSLATIONS[lang]['sol_price_label'], f"${sol_price:,.2f}", f"{sol_change:+.2f}%")
    st.metric(TRANSLATIONS[lang]['sol_block_label'], block_height)
    if current_tps is not None:
        # TPS actuel avec deux décimales
        st.metric(TRANSLATIONS[lang]['sol_tps_label'], f"{current_tps:.2f}")

# Graphique de l'évolution du TPS de Solana sur 60 dernières minutes
from utils import visuals
fig = visuals.make_tps_chart(samples, title=TRANSLATIONS[lang]['tps_chart_title'])
st.plotly_chart(fig, use_container_width=True)
