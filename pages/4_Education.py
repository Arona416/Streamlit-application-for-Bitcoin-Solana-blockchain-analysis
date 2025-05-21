import streamlit as st
from utils.language import TRANSLATIONS

# Configuration de la langue et de la page
if 'lang' not in st.session_state:
    st.session_state.lang = 'FR'
lang = st.session_state.lang
st.set_page_config(page_title=TRANSLATIONS[lang]['page_title_education'], page_icon="🔗")

# Sélecteur de langue dans la barre latérale
lang_options = {"Français": "FR", "English": "EN", "Русский": "RU"}
choice = st.sidebar.selectbox(TRANSLATIONS[lang]['language_label'], 
                              options=list(lang_options.keys()), 
                              index=list(lang_options.values()).index(lang))
st.session_state.lang = lang_options[choice]
lang = st.session_state.lang

# Titre de la page éducative
st.title(TRANSLATIONS[lang]['education_title'])

# Section : Qu'est-ce que la blockchain ?
st.header(TRANSLATIONS[lang]['edu_blockchain_title'])
st.markdown(TRANSLATIONS[lang]['edu_blockchain_text'])

# Section : Bitcoin (histoire, fonctionnement)
st.header(TRANSLATIONS[lang]['edu_bitcoin_title'])
st.markdown(TRANSLATIONS[lang]['edu_bitcoin_text'])

# Section : Solana (architecture, différences)
st.header(TRANSLATIONS[lang]['edu_solana_title'])
st.markdown(TRANSLATIONS[lang]['edu_solana_text'])
