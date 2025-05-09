from solana.rpc.api import Client

SOLANA_RPC_URL = "https://api.mainnet-beta.solana.com"   # endpoint(URL) RPC public

# Créer un client RPC Solana (connexion au cluster Mainnet-beta)
client = Client(SOLANA_RPC_URL)

def fetch_solana_performance(n_samples = 60):
    "Recupere les n_samples derniers echantillons de performance du reseau Solana par defaut."
    resp = client.get_recent_performance_samples(limit=n_samples)
    samples = resp.value # pour avoir liste des echantillons de perf
    return samples

