import yfinance as yf
import matplotlib.pyplot as plt
import numpy as np

def telecharger_et_afficher(ticker, date_debut, date_fin):
    """
    Télécharge les données historiques d'un stock et affiche le graphique de l'évolution des cours.
    Utilise les données brutes (Close) sans ajustement.
    """
    try:
        # Télécharger les données
        donnees = yf.download(ticker, start=date_debut, end=date_fin)

        if donnees.empty:
            print("Aucune donnée téléchargée. Vérifiez les paramètres.")
            return None

        # Afficher le graphique de l'évolution du cours avec le prix brut (Close)
        plt.figure(figsize=(10, 6))
        plt.plot(donnees['Close'], label="Prix brut", color='blue', linewidth=1)  # Données réelles en bleu
        plt.title(f"Évolution des cours bruts de {ticker}")
        plt.xlabel("Date")
        plt.ylabel("Prix brut")
        plt.legend()
        plt.grid(True)
        plt.show()

        return donnees
    except Exception as e:
        print(f"Download or display error : {e}")
        return None


def calculer_et_afficher_log_returns(donnees):
    """
    Calcule les rendements logarithmiques à partir des prix bruts (Close) et les affiche.
    """
    try:
        if 'Close' not in donnees.columns:
            print("The data must contain a 'Close' column.")
            return

        # Calcul des log returns à partir des prix bruts
        log_returns = np.log(donnees['Close'] / donnees['Close'].shift(1))

        # Affichage du graphique des log returns
        plt.figure(figsize=(10, 6))
        plt.plot(log_returns, label="Log Returns", color='orange')
        plt.title("Évolution des rendements logarithmiques")
        plt.xlabel("Date")
        plt.ylabel("Log Returns")
        plt.legend()
        plt.grid(True)
        plt.show()

        return log_returns
    except Exception as e:
        print(f"Error when calculating or displaying log returns : {e}")
        return None


def generer_trajectoires_monte_carlo(prix_initial, mu, sigma, n_jours, n_trajectoires, dates):
    """
    Génère des trajectoires de Monte Carlo en utilisant un mouvement brownien géométrique
    et les dates des données historiques.
    """
    trajectoires = []
    for _ in range(n_trajectoires):
        trajectoire = [prix_initial]  # Initialiser avec le prix de départ (ici, le prix du premier jour des données historiques)
        for t in range(1, n_jours):
            prix_suivant = trajectoire[-1] * np.exp((mu - 0.5 * sigma**2) + sigma * np.random.normal())
            trajectoire.append(prix_suivant)
        trajectoires.append(trajectoire)
    
    # Assurer que les trajectoires utilisent les mêmes dates que les données historiques
    dates_simulation = dates
    return trajectoires, dates_simulation


def afficher_graphique_monte_carlo(trajectoires, dates_simulation, donnees_historique, titre="Simulations de Monte Carlo"):
    """
    Affiche le graphique des trajectoires simulées de Monte Carlo.
    """
    # Aligner les trajectoires simulées avec les dates des données historiques
    plt.figure(figsize=(10, 6))
    
    # Afficher les trajectoires simulées avec des couleurs aléatoires
    for trajectoire in trajectoires:
        plt.plot(dates_simulation, trajectoire, alpha=0.4, color=np.random.rand(3,))  # Couleur aléatoire

    # Afficher les données réelles (historique) avec un style modifié
    plt.plot(donnees_historique['Close'], label="Données réelles", color="red", linewidth=2)  # Données réelles en bleu et plus fines

    plt.title(titre)
    plt.xlabel("Date")
    plt.ylabel("Prix brut")
    plt.legend()
    plt.grid(True)
    plt.show()


# Paramètres de téléchargement
ticker = input("What ticker have you chosen ?\n")
date_debut = input("What is the start date in YYYY-MM-DD format ?\n")
date_fin = input("What is the end date in YYYY-MM-DD format ?\n")

# Téléchargement des données et affichage du graphique des prix bruts
donnees = telecharger_et_afficher(ticker, date_debut, date_fin)

if donnees is not None:
    # Calcul et affichage des log returns
    log_returns = calculer_et_afficher_log_returns(donnees)

    # Paramètres pour la simulation de Monte Carlo
    prix_initial = donnees['Close'].iloc[0]  # Premier prix brut (pour partir du même point que le premier jour des données réelles)
    mu = log_returns.mean()  # Rendement moyen basé sur les log returns
    sigma = log_returns.std()  # Volatilité basée sur les log returns
    n_jours = len(donnees)  # Nombre de jours de la période
    n_trajectoires = int(input("How many trajectories need to be generated? \n"))  # Nombre de trajectoires de Monte Carlo à générer

    # Générer les trajectoires de Monte Carlo et obtenir les dates simulées
    trajectoires, dates_simulation = generer_trajectoires_monte_carlo(prix_initial, mu, sigma, n_jours, n_trajectoires, donnees.index)

    # Afficher les trajectoires simulées de Monte Carlo
    afficher_graphique_monte_carlo(trajectoires, dates_simulation, donnees, titre=f"Monte Carlo simulations for {ticker}")