# Saisie des valeurs des goods
Good_1 = float(input("What's the Price of good 1?"))
Good_2 = float(input("What's the Price of good 2?"))
Budget = float(input("What's the budget?"))

# Calcule de la valeur total des goods
Total_price_of_goods = (float(Good_1+Good_2))

#Affichage du total des goods et de si le budget est supérieur ou non
print("The total price of the goods are",Total_price_of_goods)
print(bool(Budget > Good_1 + Good_2))