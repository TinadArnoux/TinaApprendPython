"""import pandas as pd

# Lire le fichier Excel en spécifiant les types de données
df = pd.read_excel('chargementPosts.xlsx', dtype={'texte': str, 'date': 'datetime64[ns]'})

# Afficher les données de la colonne "texte"
print(df['texte'])

# Filtrer les données pour les dates après une certaine date
date_seuil = pd.to_datetime('2023-01-01')
df_filtre = df[df['date'] > date_seuil]
print(df_filtre)"""

import datetime

# magestion de BDD
from gestionBDD import Database
from gestionExcel import FichierExcel

# Chemin vers votre fichier .db
db = Database('Mes_Tweets.db')
print("BDD : Mes_Tweets.db")


# Ouvrir le fichier Excel
Fichier = 'chargementPosts'
fichierComplet = Fichier + ".xlsx"
# formater les nouveau nom et chemin
# Obtenir la date actuelle
date_aujourdhui = (datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S"))
ancienChemin = "C:/Users/mchri/PycharmProjects/PythonProject1/" + fichierComplet
nouveauChemin = "C:/Users/mchri/PycharmProjects/PythonProject1/archive_excel/"
nouveauNom = f"{Fichier}_traite_{date_aujourdhui}.xlsx"

# lire le fichier
try:
    FichierExcel.ouvre_et_lit_fichier(fichierComplet)
except:
    # créer fichire vide
    FichierExcel.cree_fichier_vide(fichierComplet)
# déplacer le fichier lu
FichierExcel.deplacer_et_renommer_fichier(ancienChemin, nouveauChemin, nouveauNom)
#créer fichire vide
FichierExcel.cree_fichier_vide(fichierComplet)
