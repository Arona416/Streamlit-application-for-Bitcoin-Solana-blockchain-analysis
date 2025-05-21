import requests
import streamlit as st

@st.cache_data(ttl=300)
def get_btc_stats():
    """Récupère les statistiques globales de Bitcoin via l'API Blockchair."""
    try:
        res = requests.get("https://api.blockchair.com/bitcoin/stats")
        res.raise_for_status()
    except Exception as e:
        print("Error fetching Bitcoin stats:", e)
        return None
    data = res.json().get("data", {})
    # Retourner un dictionnaire avec les informations clés (dernier bloc et tx en mempool)
    return {
        "blocks": data.get("blocks"),
        "mempool_transactions": data.get("mempool_transactions")
    }

@st.cache_data(ttl=300)
def get_btc_mempool_data(days=7):
    """Récupère l'historique du nombre de transactions en mempool Bitcoin sur `days` jours."""
    url = f"https://api.blockchain.info/charts/mempool-count?timespan={days}days&format=json&sampled=true"
    try:
        res = requests.get(url)
        res.raise_for_status()
    except Exception as e:
        print("Error fetching mempool data:", e)
        return []
    data = res.json()
    # La réponse contient une liste de valeurs avec timestamp 'x' et valeur 'y'
    return data.get("values", [])
