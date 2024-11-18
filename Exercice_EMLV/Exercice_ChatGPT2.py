"""Situation
Tu es analyste en gestion de portefeuille, et tu souhaites évaluer la performance d’un portefeuille d’actions 
en termes de rendements individuels et global. Tu vas calculer le rendement de plusieurs actions différentes 
que tu possèdes et déterminer la performance globale de ton portefeuille.

Consigne
Crée un programme avec des fonctions pour :

Calculer le rendement individuel d’une action en fonction de son prix d’achat, de son prix de vente et du 
nombre d’actions détenues.
Calculer le rendement total de l’ensemble du portefeuille en tenant compte de tous les rendements individuels 
pondérés par leur montant investi initialement.

Objectif
Le programme doit permettre d’entrer plusieurs transactions, d’obtenir les rendements individuels, puis de 
calculer et d’afficher le rendement global du portefeuille."""

# --- fonction pour calculer le rendement individuel d'une action ---
def calcul_du_rendement_individuel(nombre_daction_acheté, prix_dachat_unitaire, prix_de_vente_unitaire):
    # Calcul du rendement individuel pour ce projet
    bénéfice_dégagé = (prix_de_vente_unitaire * nombre_daction_acheté) - (prix_dachat_unitaire * nombre_daction_acheté)
    rendement_individuel = (bénéfice_dégagé / (prix_dachat_unitaire * nombre_daction_acheté)) * 100  # Rendement en pourcentage
    return rendement_individuel

# --- fonction pour calculer le rendement collectif pondéré ---
def calcul_du_rendement_collectif():
    somme_rendement_pondéré = 0
    somme_investis = 0
    bénéfice_total = 0  # Variable pour accumuler le bénéfice total

    while True:
        # Demander les informations nécessaires à l'utilisateur pour chaque investissement
        nombre_daction_acheté = int(input("Nombre d'actions achetées : "))
        prix_dachat_unitaire = float(input("Prix d'achat unitaire : "))
        prix_de_vente_unitaire = float(input("Prix de vente unitaire : "))
        
        # Calcul du rendement individuel pour cet investissement
        rendement_individuel = calcul_du_rendement_individuel(nombre_daction_acheté, prix_dachat_unitaire, prix_de_vente_unitaire)
        
        # Calcul du montant investi dans ce projet
        montant_investi = nombre_daction_acheté * prix_dachat_unitaire
        
        # Accumuler les résultats
        somme_rendement_pondéré += rendement_individuel * montant_investi
        somme_investis += montant_investi
        bénéfice_total += (prix_de_vente_unitaire * nombre_daction_acheté) - (prix_dachat_unitaire * nombre_daction_acheté)  # Bénéfice total
        
        # Demander à l'utilisateur s'il a d'autres projets
        autre_projet = input("Avez-vous d'autres investissements ? (Oui/Non) : ").strip().lower()
        
        # Vérification que la réponse est bien "oui" ou "non"
        while autre_projet not in ["oui", "non"]:
            print("Répondez à la question par 'Oui' ou 'Non'.")
            autre_projet = input("Avez-vous d'autres investissements ? (Oui/Non) : ").strip().lower()
        
        # Si l'utilisateur n'a plus d'autres investissements, on sort de la boucle
        if autre_projet == "non":
            break  # Sortir de la boucle si l'utilisateur dit "Non"
    
    # Calcul du rendement collectif pondéré en pourcentage
    rendement_collectif_pondéré = somme_rendement_pondéré / somme_investis  # Rendement global pondéré
    rendement_collectif_pondéré = round(rendement_collectif_pondéré, 2)  # Arrondir pour avoir deux décimales
    
    # Affichage des résultats
    print(f"\nLe rendement collectif pondéré est de {rendement_collectif_pondéré}%")
    print(f"Bénéfice total réalisé : {bénéfice_total:.2f}€")
    print(f"Montant total investi : {somme_investis:.2f}€")

# Appel de la fonction principale
calcul_du_rendement_collectif()

