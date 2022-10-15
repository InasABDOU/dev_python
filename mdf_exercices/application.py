# importation des modules
from calcul_de_force import calculer_force

# calcul de la force en fonction de la pression et la surface

# demander a l'utilisateur de renseigner la pression et la surface
P=float(input("la valeur de la pression : "))
s=float(input("la valeur de la surface : "))

# calcul de la force
F= calculer_force(pression=P, surface=s)
print("la force est : ",F)

