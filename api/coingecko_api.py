import requests
import streamlit as st

@st.cache_data(ttl=300)
def get_crypto_prices(ids):
    """
    Récupère le prix USD actuel et la variation 24h pour une liste de cryptos depuis CoinGecko.
    `ids` doit être une liste des identifiants CoinGecko (ex: ['bitcoin', 'solana']).
    """
    ids_param = ",".join(ids)
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={ids_param}&vs_currencies=usd&include_24hr_change=true"
    try:
        res = requests.get(url)
        res.raise_for_status()
    except Exception as e:
        print("Error fetching prices from CoinGecko:", e)
        return {}
    # Retour du dictionnaire des prix, e.g. {'bitcoin': {'usd': ..., 'usd_24h_change': ...}, ...}
    return res.json()

@st.cache_data(ttl=1800)
def get_price_history(coin, days):
    """
    Récupère l'historique du prix en USD pour `coin` sur les `days` derniers jours (données quotidiennes).
    """
    url = f"https://api.coingecko.com/api/v3/coins/{coin}/market_chart?vs_currency=usd&days={days}&interval=daily"
    try:
        res = requests.get(url)
        res.raise_for_status()
    except Exception as e:
        print(f"Error fetching historical prices for {coin}:", e)
        return []
    data = res.json()
    prices = data.get("prices", [])  # liste de [timestamp, price]
    history = []
    from datetime import datetime
    for timestamp, price in prices:
        # Convertir le timestamp (ms) en objet datetime Python
        dt = datetime.fromtimestamp(timestamp/1000)
        history.append({"date": dt, "price": price})
    return history
