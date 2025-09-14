
# AI-powered
This application uses a lightweight AI model to detect and counter persistent AI attacks that evade traditional controls.
=======
# Eurocybersecurite AI Cybersecurity Application 🤖🛡️

[![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![HuggingFace](https://img.shields.io/badge/Model-HuggingFace-yellow.svg)](https://huggingface.co/)
[![GitHub stars](https://img.shields.io/github/stars/eurocybersecurite/AI-powered.svg)](https://github.com/eurocybersecurite/AI-powered/stargazers)

## 🔗 Dépôt GitHub

Vous pouvez trouver le code source de cette application sur GitHub : [https://github.com/eurocybersecurite/AI-powered](https://github.com/eurocybersecurite/AI-powered)

---

## 🌐 Description

**Eurocybersecurite AI Cybersecurity Application** est une application de cybersécurité basée sur l’intelligence artificielle.
Elle utilise un modèle léger pré-entraîné de **Hugging Face** pour :

* Détecter des menaces cachées dans des données textuelles
* Identifier des attaques persistantes qui échappent aux contrôles traditionnels
* Fournir une analyse rapide et automatisée des risques

Objectif : offrir une **protection proactive** et accessible aux équipes sécurité.

---

## 🔧 Fonctionnalités principales

* 📊 Analyse automatique de textes
* 🤖 Détection par modèle IA (Hugging Face)
* ⚡ Application légère et rapide
* 🌍 Interface web simple d’utilisation (Flask)
* 🛡️ Détection d’attaques persistantes basées sur l’IA
* 📑 Rapport instantané avec niveau de menace

---

## ⚙️ Installation

### 🔧 Prérequis

* Python **3.11+**
* Pip & virtualenv

### Étapes

```bash
# 1. Créer un environnement virtuel
python3 -m venv venv

# 2. Activer l’environnement
source venv/bin/activate   # Linux/macOS
venv\Scripts\activate      # Windows

# 3. Installer les dépendances
pip install -r requirements.txt
```

---

## 🚀 Utilisation

1. Lancer l’application :

```bash
python main.py
```

2. Ouvrir le navigateur : [http://localhost:5577](http://localhost:5577)
3. Entrer un texte à analyser dans le champ **"Enter data to analyze"**
4. Cliquer sur **Run Analysis**
5. Lire le rapport affiché : niveau de menace + type de modèle IA utilisé

---

## 🗺️ Feuille de route (Roadmap)

* [x] Analyse de textes par IA Hugging Face
* [x] Interface web Flask
* [ ] Support multi-langues
* [ ] Intégration d’alertes par email/Slack
* [ ] Amélioration des modèles avec fine-tuning
* [ ] Export avancé des rapports (PDF/CSV)

---

## � Nouveautés

* Ajout d'un système de notification basique affichant l'historique des notifications sur la page d'accueil.

---

## �📦 Déploiement

### 📤 PyPI

```bash
pip install twine
python setup.py sdist bdist_wheel
twine upload dist/*
```

### 🌐 GitHub

```bash
git init
git add .
git commit -m "Initial commit"
git remote add origin <repository_url>
git push -u origin main
```

---

## 🤝 Contribution

Les contributions sont les bienvenues !
Merci d’ouvrir une **issue** ou une **Pull Request** pour proposer vos améliorations.

👤 **Auteur principal :** Abdessemed Mohamed Redha
📧 **Contact :** [mohamed.abdessemed@eurocybersecurite.fr](mailto:abdessemed.mohamed@eurocybersecurite.fr)

---

## 📜 Licence

Ce projet est sous licence **MIT**.
Voir [LICENSE](LICENSE) pour plus de détails.
