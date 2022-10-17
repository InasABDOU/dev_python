# imprtation des modules
from calcul_de_longueur import calculer_longueur
from ecrire_dans_image import ecrire_image

# demander a l'utilisateur de renseigner le diametre1,la vitesse1,alpha en degre et le coefficient
D1=float(input("enter la valeur de diametre 1 : "))
V1=float(input("entrer la valeur de vitesse 1 : "))
a=float(input("entrer la valeur de alpha en degré : "))
k=float(input("entrer la valeur de coefficient : "))

# calcul de la longueur en fonction des diametres ,la vitesse et l'ongle alpha
L = calculer_longueur(diametre1 = D1, vitesse1 = V1, alpha = a, coefficient = k)

# affichage des résultats 
print()
print(f'la vitesse2 est : {L["vitesse2"]} m/s')
print(f'le diametre2 est : {L["diametre2"]} m')
print(f'la longueur est : {L["longueur"]} m')
print(f'la variation de la pression est : {L["var_pression"]} Pa')

# Ecrire les information (D1, V1, L, V2 et a) dans une image
ecrire_a = ecrire_image(valeur_a_insert = f" = {a}", position_text=[525,53], size_text=14)
ecrire_D1 = ecrire_image(valeur_a_insert = f" = {D1}", position_text=[148,156], size_text=16)
ecrire_V1 = ecrire_image(valeur_a_insert = f" = {V1}", position_text=[194,191], size_text=16)
ecrire_L = ecrire_image(valeur_a_insert = f" = {round(L['longueur'],4)}", position_text=[552,212], size_text=16)
ecrire_V2 = ecrire_image(valeur_a_insert = f" = {round(L['vitesse2'],4)}", position_text=[948,197], size_text=16)