"""Exercice
Tu travailles comme analyste financier et tu souhaites évaluer le résultat financier d’une transaction 
d'actions. Tu achètes un certain nombre d'actions à un prix donné et tu les revends plus tard à un autre prix.
Ton programme Python devra calculer le coût final de la transaction et indiquer si celui-ci 
est profitable, neutre ou déficitaire.

Indice
Calcule d'abord la différence entre le prix de vente et le prix d'achat pour obtenir le résultat par action."""



# --- Saisie des données d'achat ---

while True:
    try:
        prix_action_initial = float(input(f"Quelle est le prix unitaire initial de l'action?\n"))
        break
    except ValueError:
        print("Veuillez entrer un prix d'action valide.")

while True:
    try:
        nombre_action_acheté = int(input("Quelle est le nombre d'action acheté?\n"))
        break
    except ValueError:
        print("Veuillez entrer un nombre d'action valide.")

# --- Calcul du total investi ---

total_investi = prix_action_initial * nombre_action_acheté
print(f"Vous avez investi un total de {total_investi:.2f}€\n")

# --- Saisie des données de revente ---

while True:
    try:
        prix_action_revendu = float(input("A quelle prix unitaire les actions ont été revendu ?\n"))
        break
    except ValueError:
        print("Veuillez entrer un nombre valide.")

# Calcul et affichage du bénéfice dégagé

bénéfice_dégagé = (prix_action_revendu - prix_action_initial) * nombre_action_acheté
Montant_total_final = bénéfice_dégagé + total_investi
print(f"Le bénéfice réalisé est de {bénéfice_dégagé:.2f}€ pour un total de {Montant_total_final:.2f}€\n")

# --- Calcul et évaluation du bénéfice ---

valeur_finale = nombre_action_acheté * prix_action_revendu
pourcentage_réalisé = (bénéfice_dégagé / total_investi) * 100

if bénéfice_dégagé > 0 :
    print(f"Le projet est profitable de {pourcentage_réalisé:.2f}%")
elif bénéfice_dégagé == 0 :
    print("Le projet est neutre car il n'as pas réalisé de bénéfice")
else :
    print(f"Le projet est déficitaire de {pourcentage_réalisé:.2f}%")
