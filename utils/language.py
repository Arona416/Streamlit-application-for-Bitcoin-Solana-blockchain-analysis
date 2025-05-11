TRANSLATIONS = {
    "FR": {
        "lang_name": "Français",
        "welcome_title": "Analyse blockchain Bitcoin et Solana",
        "welcome_text": "Bienvenue ! Ceci est une application interactive pour visualiser les données blockchain Bitcoin et Solana.",
        "menu_bitcoin": "Statistiques sur le Bitcoin",
        "menu_solana": "Performance du réseau Solana",
        "menu_comparaison": "Comparaison des deux blockchains",
        "menu_education": "Section éducative"
    },
    "EN": {
        "lang_name": "English",
        "welcome_title": "Blockchain analysis: Bitcoin and Solana",
        "welcome_text": "Welcome! This is an interactive app to visualize blockchain data from Bitcoin and Solana.",
        "menu_bitcoin": "Bitcoin Statistics",
        "menu_solana": "Solana Network Performance",
        "menu_comparaison": "Blockchain Comparison",
        "menu_education": "Educational Section"
    },
    "RU": {
        "lang_name": "Русский",
        "welcome_title": "Анализ блокчейнов Bitcoin и Solana",
        "welcome_text": "Добро пожаловать! Это интерактивное приложение для анализа данных блокчейнов Bitcoin и Solana.",
        "menu_bitcoin": "Статистика по Биткойну",
        "menu_solana": "Производительность сети Solana",
        "menu_comparaison": "Сравнение блокчейнов",
        "menu_education": "Образовательный раздел"
    }
}

DEFAULT_LANG = "RU"

def get_text(key, lang=None):
    lang = lang or DEFAULT_LANG
    return TRANSLATIONS.get(lang, {}).get(key, f"[{key}]")
