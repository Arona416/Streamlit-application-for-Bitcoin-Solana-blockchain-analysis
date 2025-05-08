# Streamlit-application-for-Bitcoin-Solana-blockchain-analysis
Interactive blockchain analytics app built with Streamlit, focused on Bitcoin and Solana. It lets users explore live stats, compare performance (TPS, fees, blocks, etc.), and access a multilingual educational section (🇷🇺🇫🇷🇬🇧) covering blockchain, Bitcoin and cryptocurrencies.


from textwrap import dedent

readme_content = dedent("""
# 📊 Blockchain Dashboard App – Bitcoin & Solana

**Langues disponibles : Français 🇫🇷 | Anglais 🇬🇧 | Русский 🇷🇺**

Une application interactive développée avec **Python** et **Streamlit**, permettant d’analyser et visualiser les données blockchain des réseaux **Bitcoin** et **Solana** en temps réel.

## 🚀 Fonctionnalités

- 🔄 **Connexion à des API blockchain** (Blockchair, Solana JSON RPC)
- 📦 **Extraction, traitement et stockage** de données on-chain (transactions, blocs, adresses, frais, etc.)
- 📊 **Visualisation interactive** avec Streamlit + Plotly/Altair
- 🌐 **Interface multilingue** (FR / EN / RU) sélectionnable par l'utilisateur
- 📚 **Section éducative intégrée** sur la blockchain, Bitcoin et les cryptomonnaies
- 🧭 **Navigation intuitive** avec menu et sous-menus
- ☁️ **Déployable facilement** sur Streamlit Cloud

## 🧱 Technologies utilisées

- Python 3.10+
- Streamlit
- Requests
- Pandas / NumPy
- Plotly / Altair
- SQLite (ou stockage mémoire via DataFrame)
- API externes (Blockchair, Solana RPC)

## 🧭 Structure du projet

