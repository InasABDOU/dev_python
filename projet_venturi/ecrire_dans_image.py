# Importing the PIL library
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

def ecrire_image(valeur_a_insert, 
                 size_text, 
                 position_text, 
                 chemin_image = './images/venturi', 
                 chemin_ttf = './images/arial_bold.ttf', 
                 text_coleur = 'black',
                 extension_image = '.jpg'):
    try:
        # Ouvrir l'image
        image = Image.open(chemin_image + extension_image)
        # Appeler la méthode draw pour ajouter du texte dans une image
        I1 = ImageDraw.Draw(image)
        # Personnalisation du style et de la taille de la police
        font = ImageFont.truetype(chemin_ttf, int(size_text))
        # Ajouter du texte à l'image
        I1.text(tuple(position_text), valeur_a_insert, font=font, fill =text_coleur)
        # Sauvegarder l'image éditée
        image.save(chemin_image + extension_image)

    except Exception as e:
        
        return f"le système a rencontre l'erreur suivante : {e}"

