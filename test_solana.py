from api.solana_api import fetch_solana_performance, get_current_tps

samples = fetch_solana_performance(n_samples=5) # recuperer 5 derniers echantillons
print("Ehantillons de performance Solona:", samples)

current_tps = get_current_tps()
print(f"TPS actuel estime: {current_tps:.2f} tx/s")