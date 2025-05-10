import os
import requests
from solana.rpc.api import Client
from dotenv import load_dotenv

#chargement des variables d'environnement 
load_dotenv()

# Url RPC public du reseau Solana (Mainnet beta)
SOLONA_RPC_URL = os.getenv("SOLANA_RPC_URL", "https://api.mainnet-beta.solana.com")

# creation  d'un client RPC Solana 
client = Client(SOLONA_RPC_URL)

def fetch_solana_performance(n_samples=60):
    """ Recuperation des n_samples derniers echantillons de performance du reseau Solona.
    Par defaut , environ 60 echantillons 
    """
    
    resp = client.get_recent_performance_samples(limit=n_samples)

    samples = resp.value # liste d'objet rpcperfornamance
    # Convertir en une liste de dict pour faciliter l'exploitatiom 

    perf_list = [
        {
            "slot": sample.slot, 
            "num_transactions": sample.num_transactions, 
            "num_slots": sample.num_slots, 
            "sample_period_secs": sample.sample_period_secs,
            "num_non_vote_tx": getattr(sample, "num_non_vote_transactions", None)

        }
        for sample in samples 
    ]
    return perf_list
def get_current_tps():
    """
    Calcule le TPS (transaction par seconde) moyen recent sur solona.
    """
    resp = client.get_recent_performance_samples(limit =1)
    latest_sample = resp.value[0] # le plus recent exhantillonde performance
    # Calcul du TPS moyen sur la fenêtre de l'échantillon (normalement sample_period_secs = 60)
    tps = latest_sample.num_transactions  / latest_sample.sample_period_secs
    return tps


COINGECKO_PRICE_SOL_URL = os.getenv("COINGECKO_API_URL", "https://api.coingecko.com/api/v3")
COINGECKO_PRICE_SOL_URL += "/simple/price?ids=solana&vs_currencies=usd"

def fetch_solona_price_usd():
    """Recuperation du prix actuel de solana en USD VIA CoinGecko"""
    res = requests.get(COINGECKO_PRICE_SOL_URL)
    if res.status_code != 200:
        raise Exception(f"Erreur API CoinGecko: {res.status_code}")
    price_data = res.json()
    sol_price = price_data.get("solana, {}").get("usd")
    return sol_price