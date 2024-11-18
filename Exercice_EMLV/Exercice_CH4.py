# Saisie du nombre d'années et du taux d'intérêt
n = float(input("What's the numbers of years ? "))
i = float(input("What's the interest rate ? "))
          
# Affichage et calcul du résultat  
print(float(17500*(1+(i/100))**n))