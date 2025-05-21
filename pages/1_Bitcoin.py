import streamlit as st
from utils.language import TRANSLATIONS
from api import blockchair_api, coingecko_api

# Configuration de la langue et de la page
if 'lang' not in st.session_state:
    st.session_state.lang = 'FR'
lang = st.session_state.lang
st.set_page_config(page_title=TRANSLATIONS[lang]['page_title_bitcoin'], page_icon="🔗")

# Sélecteur de langue dans la barre latérale
lang_options = {"Français": "FR", "English": "EN", "Русский": "RU"}
choice = st.sidebar.selectbox(TRANSLATIONS[lang]['language_label'], 
                              options=list(lang_options.keys()), 
                              index=list(lang_options.values()).index(lang))
st.session_state.lang = lang_options[choice]
lang = st.session_state.lang  # Mise à jour de la langue après sélection

# Titre de la page Bitcoin
st.title(TRANSLATIONS[lang]['bitcoin_title'])

# Appel des API pour obtenir les données Bitcoin actuelles
btc_stats = blockchair_api.get_btc_stats()        # Statistiques blockchain Bitcoin (Blockchair)
prices = coingecko_api.get_crypto_prices(['bitcoin'])  # Prix Bitcoin en USD et variation 24h (CoinGecko)

# Vérification que les données ont bien été récupérées
if btc_stats and prices:
    btc_price = prices['bitcoin']['usd']
    btc_change = prices['bitcoin']['usd_24h_change']
    # Affichage des métriques principales de Bitcoin (prix, dernier bloc, transactions mempool)
    st.metric(TRANSLATIONS[lang]['btc_price_label'], f"${btc_price:,.2f}", f"{btc_change:+.2f}%")
    st.metric(TRANSLATIONS[lang]['btc_block_label'], btc_stats['blocks'])
    st.metric(TRANSLATIONS[lang]['btc_mempool_label'], btc_stats['mempool_transactions'])

# Récupération des données historiques de la mempool Bitcoin pour le graphique (7 derniers jours)
mempool_data = blockchair_api.get_btc_mempool_data(days=7)

# Génération du graphique Plotly de l'évolution du nombre de transactions en mempool
from utils import visuals
fig = visuals.make_mempool_chart(mempool_data, title=TRANSLATIONS[lang]['mempool_chart_title'])
st.plotly_chart(fig, use_container_width=True)
