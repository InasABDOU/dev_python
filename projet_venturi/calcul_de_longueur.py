"""
Created on Sat Oct 15 13:15:20 2022

@author: Inas ABDOU
"""

# imprtation des modules
from math import sqrt,tan

def calculer_longueur(diametre1,vitesse1,alpha,coefficient,rho=10**3):
    
    try:
        # calcul de la vitesse 2
        vitesse2 = coefficient*vitesse1
        # calcul du diametre 2
        diametre2 = sqrt(vitesse2/vitesse1)
        # calcul de la longueur
        longueur = -diametre1/2*(tan(alpha))*(diametre2/diametre1)-1
        # calcul de la variation de pression selon theoreme de Bernoulli
        var_pression = rho*((vitesse2**2)-(vitesse1**2))/2
        
        return {"vitesse2" : vitesse2,
                "diametre2" : diametre2,
                "longueur" : longueur,
                "var_pression" :var_pression}
    
    except Exception as e:
        
        return f"le système a rencontre l'erreur suivante : {e}"