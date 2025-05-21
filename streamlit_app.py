import streamlit as st
from utils.language import TRANSLATIONS

# Configuration de la page principale (titre de l'onglet, icône, mise en page large)
st.set_page_config(page_title=TRANSLATIONS['FR']['page_title_home'], page_icon="🔗", layout="wide")

# Initialisation de la langue par défaut (français) si non encore sélectionnée
if 'lang' not in st.session_state:
    st.session_state['lang'] = 'FR'
lang = st.session_state['lang']  # Code langue actuel (FR, EN ou RU)

# Sélecteur de langue dans la barre latérale
lang_options = {"Français": "FR", "English": "EN", "Русский": "RU"}
selected_language = st.sidebar.selectbox(TRANSLATIONS[lang]['language_label'], 
                                         options=list(lang_options.keys()), 
                                         index=list(lang_options.values()).index(lang))
# Mise à jour de la langue choisie
st.session_state['lang'] = lang_options[selected_language]
lang = st.session_state['lang']

# Titre principal de la page d'accueil
st.title(TRANSLATIONS[lang]['home_title'])
# Texte d'introduction sur la page d'accueil
st.write(TRANSLATIONS[lang]['home_intro'])

# Présentation des quatre sections de l'application sous forme de liste à puces
st.markdown(f"- **{TRANSLATIONS[lang]['home_bitcoin_title']}** – {TRANSLATIONS[lang]['home_bitcoin_desc']}")
st.markdown(f"- **{TRANSLATIONS[lang]['home_solana_title']}** – {TRANSLATIONS[lang]['home_solana_desc']}")
st.markdown(f"- **{TRANSLATIONS[lang]['home_comparison_title']}** – {TRANSLATIONS[lang]['home_comparison_desc']}")
st.markdown(f"- **{TRANSLATIONS[lang]['home_education_title']}** – {TRANSLATIONS[lang]['home_education_desc']}")
