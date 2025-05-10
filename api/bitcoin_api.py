import os 
import requests
from dotenv import load_dotenv

# Charger les variables d'environnement 
load_dotenv()

# URL de L'endpoint Blockchair pour les statistiques Bitcoin
BLOCKCHAIR_STATS_URL = os.getenv("BTC_STATS_URL", "https://api.blockchair.com/bitcoin/stats")

#URL de l'endpoint Coingecko pour recuperer le prix du bitcoin en USD ( we use API "simple/price")
COINGECKO_PRICE_URL = os.getenv("COINGECKO_API_URL",  "https://api.coingecko.com/api/v3")
COINGECKO_PRICE_URL += "/simple/price?ids=bitcoin&vs_currencies=usd"


def fetch_bitcoin_stats():
    """Recupere les statistique principales de bitcoin via Blockchair"""
    res = requests.get(BLOCKCHAIR_STATS_URL)
    if res.status_code != 200:
        raise Exception (f"Erreur API Blockchair: {res.status_code}")
    # L'API renvoie un JSON dont la cle "data" contient les statistiques
    data = res.json().get("data", {})
    return data # renvoie un edictionnaire avec les stats Bitcoins (blocks, mempool ...)


def fetch_bitcoin_price_usd():
    """recupere le prix actuel du Bitcoin en usd via l'API CoinGecko."""
    res = requests.get(COINGECKO_PRICE_URL)
    if res.status_code != 200:
        raise Exception (f"Erreur API Coingecko: {res.status_code}")
    price_data = res.json()
    
    btc_price = price_data.get("bitcoin",{}).get("usd")
    return btc_price