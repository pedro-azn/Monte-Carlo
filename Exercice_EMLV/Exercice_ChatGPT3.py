'''Exercice : Filtrer et transformer une liste de produits
Imagine que tu travailles sur un programme de gestion pour un magasin. Dans une liste, tu as plusieurs 
produits, et chaque produit est décrit par un nom et un prix en euros.

Objectif
Filtrer les produits dont le prix est supérieur à un certain montant donné (que l'utilisateur spécifie).
Appliquer une réduction de prix de 10% aux produits qui dépassent ce montant, 
tout en gardant les autres inchangés.
Afficher les produits (nom et prix) après application du filtre et de la réduction.'''

'''Étapes pour t’aider à démarrer
Demande à l'utilisateur le prix minimum pour appliquer la réduction.
Filtre la liste de produits avec filter() et une fonction lambda.
Applique la réduction avec map() et une fonction lambda sur les produits filtrés.'''


# Saisie du prix minimum
while True:
    try:
        prix_minimum = float(input("Quelle est le prix minimum pour bénéficier d'une réduction ?\n").strip())
        break  # Sortie de la boucle si la conversion réussit
    except ValueError:
        print("Veuillez saisir un prix valide")


# Création des listes
liste_produits_promotionné = []        # Liste vide pour stocker les produits promotionné
liste_produits_non_promotionné = []    # Liste vide pour stocker les produits non promotionné

# Boucle générale 
while True:

    # Sous-boucle pour saisie du prix du produit avec gestion d'erreur
    while True:
        try:
            prix_produit = float(input("Quelle est le prix du produit ?\n").strip())
            break
        except ValueError:
            print("Veuillez saisir un prix valide pour le produit")


    # Saisie du nom du produit
    nom_produit = input("Quelle est le nom de ce produit ? \n").strip().capitalize()

    # Ajout du produit à la liste promotionné
    if prix_produit >= prix_minimum :
        liste_produits_promotionné.append({"nom": nom_produit, "prix": prix_produit})

    # Ajout du produit à la liste non-promotionné
    if prix_produit < prix_minimum :
        liste_produits_non_promotionné.append({"nom": nom_produit, "prix": prix_produit}) 

    # Saisie de la question sur un autre produit
    autre_produit = input("Avez-vous d'autres produits ? oui/non \n").strip().lower()

    if autre_produit == "non":
        break  # Si l'utilisateur répond "non", on sort de la boucle


# Affichage de la liste des produits et prix qui seront promotionné
print("\n--- Produits pouvant bénéficier de la promotion ---")
for produit in liste_produits_promotionné :
    print(f"Produit : {produit['nom']}, Prix actuel : {produit['prix']:.2f}€")

# Affichage de la liste des produits et prix qui ne seront pas promotionné
print("\n--- Produits ne bénéficiant pas de la promotion ---")
for produit in liste_produits_non_promotionné :
    print(f"Produit : {produit['nom']}, Prix actuel : {produit['prix']:.2f}€")


# Calcul du pourcentage de réduction
pourcentage_réduction = float(input("De combien de pourcentage est la promotion ? \n")) / 100

# Création de la liste pour contenir les prix des produits remisés
liste_prix_remisé = []

# Sélection de chaque produit éligible à la promotion
for produit in liste_produits_promotionné :

    # Calcul du nouveau prix de chaque produit
    prix_remisé = produit["prix"] * pourcentage_réduction
    
     # Ajout du produit avec le prix remisé à la liste produits_remisé
    liste_prix_remisé.append({"nom": produit ["nom"], "prix": prix_remisé})    

# Affichage des produits et leurs prix après remise
print("\n--- Produits remisés ---")
for produit in liste_prix_remisé:
    print(f"Produit promotionné : {produit["nom"]}, Prix après remise : {produit["prix"]:.2f}€")