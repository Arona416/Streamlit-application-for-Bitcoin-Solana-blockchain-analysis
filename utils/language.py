import streamlit as st

# Dictionnaires de traductions pour les textes de l'interface
TRANSLATIONS = {
        "RU": {
        "lang_name": "Русский",
        "menu_home": "Главная",
        "menu_bitcoin": "Биткоин",
        "menu_solana": "Солана",
        "menu_comparaison": "Сравнение",
        "menu_education": "Обучение",
        "welcome_title": "Анализ блокчейнов Биткоина и Соланы",
        "welcome_text": "Добро пожаловать! Это интерактивное приложение для анализа данных блокчейнов Биткоина и Соланы.",
        "btc_price": "Цена Биткоина (USD)",
        "sol_price": "Цена Соланы (USD)",
        "mempool_tx": "Неподтверждённые транзакции",
        "block_count": "Количество блоков",
        "tps_label": "Транзакций в секунду",
        "edu_title": "Образовательный раздел",
        "edu_content": "Здесь вы найдёте учебную информацию о Биткоине и Солане..."
    },

    "EN": {
        "lang_name": "English",
        "menu_home": "Accueil",
        "menu_bitcoin": "Bitcoin",
        "menu_solana": "Solana",
        "menu_comparaison": "Comparison",
        "menu_education": "Education",
        "welcome_title": "Bitcoin and Solana Blockchain Analysis",
        "welcome_text": "Welcome! This is an interactive app to analyze Bitcoin and Solana blockchain data.",
        "btc_price": "Bitcoin Price (USD)",
        "sol_price": "Solana Price (USD)",
        "mempool_tx": "Unconfirmed TX in Mempool",
        "block_count": "Block Count",
        "tps_label": "Transactions per second",
        "edu_title": "Educational Section",
        "edu_content": "Here you will find educational information about Bitcoin and Solana..."
    },
    "FR": {
        "lang_name": "Français",
        "menu_home": "Accueil",
        "menu_bitcoin": "Bitcoin",
        "menu_solana": "Solana",
        "menu_comparaison": "Comparaison",
        "menu_education": "Éducation",
        "welcome_title": "Analyse des blockchains Bitcoin et Solana",
        "welcome_text": "Bienvenue ! Cette application interactive permet d'analyser les données de Bitcoin et de Solana.",
        "btc_price": "Prix Bitcoin (USD)",
        "sol_price": "Prix Solana (USD)",
        "mempool_tx": "Transactions en mempool",
        "block_count": "Nombre de blocs",
        "tps_label": "Transactions par seconde",
        "edu_title": "Section Éducative",
        "edu_content": "Vous trouverez ici des informations pédagogiques sur Bitcoin et Solana..."
    }
}

# Langue par defaut
DEFAULT_LANG = "RU"

def get_text(key):
    """ Renvoie le texte traduit correspondant a la cle donnee, selon la langue selectionnee"""
    lang = st.session_state.get("lang", DEFAULT_LANG)
    return TRANSLATIONS.get(lang, {}).get(key, "")
