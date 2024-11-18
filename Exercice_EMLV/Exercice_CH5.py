"""
Commentaoire
"""
# Saisie de l'argent donné et du prix de l'objet
argent_donnee = float(input("Quel est le montant donné par le client ? "))
prix_objet = float(input("Quel est le prix de l'objet ? "))

# Calcul du montant de monnaie à rendre
reste = argent_donnee - prix_objet

# Calcul du nombre de billets pour chaque dénomination
billets_100 = int(reste // 100)     # Nombre de billets de 100
reste %= 100                        # Mise à jour du reste après 100

billets_10 = int(reste // 10)       # Nombre de billets de 10
reste %= 10                         # Mise à jour du reste après 10

billets_2 = int(reste // 2)         # Nombre de billets de 2
reste %= 2                          # Mise à jour du reste après 2

billets_1 = int(reste // 1)         # Nombre de billets de 1 (reste final)

# Affichage du résultat
print("Le rendu de monnaie est:")
print("Billets de 100:", billets_100)
print("Billets de 10:", billets_10)
print("Billets de 2:", billets_2)
print("Billets de 1:", billets_1)