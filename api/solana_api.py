import requests
import streamlit as st

RPC_URL = "https://api.mainnet-beta.solana.com"

@st.cache_data(ttl=60)
def get_solana_block_height():
    """Récupère le dernier numéro de bloc (block height) du réseau Solana via un appel RPC."""
    payload = {"jsonrpc": "2.0", "id": 1, "method": "getBlockHeight"}
    try:
        res = requests.post(RPC_URL, json=payload)
        res.raise_for_status()
    except Exception as e:
        print("Error fetching Solana block height:", e)
        return None
    data = res.json()
    return data.get("result")

@st.cache_data(ttl=60)
def get_solana_performance(samples=60):
    """
    Récupère les échantillons de performance récents de Solana (transactions par intervalle de 60s).
    Par défaut, récupère les `samples` derniers échantillons (ex: 60 pour ~1h).
    """
    payload = {
        "jsonrpc": "2.0",
        "id": 1,
        "method": "getRecentPerformanceSamples",
        "params": [samples]
    }
    try:
        res = requests.post(RPC_URL, json=payload)
        res.raise_for_status()
    except Exception as e:
        print("Error fetching Solana performance:", e)
        return None
    data = res.json()
    # Renvoie la liste des échantillons (dictionnaires avec numTransactions, samplePeriodSecs, etc.)
    return data.get("result", [])
