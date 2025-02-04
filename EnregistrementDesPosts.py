
import tkinter as tk
import tkinter.ttk as ttk
from datetime import datetime
from tkinter import filedialog

from gestionBDD import Database


# Bouton pour parcourir et sélectionner un fichier
def parcourir_fichier():
    fichier_selectionne = filedialog.askopenfilename()
    entree_fichier.delete(0, tk.END)
    entree_fichier.insert(0, fichier_selectionne)
    # Associer la fonction à l'événement de modification du champ de fichier


def enregistrer_donnees():
    datepost = entree_date.get()
    if not datepost:
        datepost = datetime.now()
        datepost = datetime.strftime(datepost, "%Y-%m-%d")  # Ajuster le format pour la BDD
    else:
    # validation date
        try:
            datepost = datetime.strptime(datepost, "%d%m%Y")
            datepost = datetime.strftime(datepost, "%Y-%m-%d")  # Ajuster le format pour la BDD
        # Si aucune exception levée, la date est au bon format
        except ValueError:
            label_confirmation.config(text="Format date incorrect. Format attendu 01/02/2024", fg="red")
            return

    textepost = entree_texte.get("1.0", "end-1c")  # Récupérer tout le texte dans le Text
    # texte saisi ?
    if not textepost:
        # Message d'erreur
        label_confirmation.config(text="Le texte est vide", fg="red")
        return

    cheminimage = entree_fichier.get()
    # Vérification si un fichier a été sélectionné
    if not cheminimage:
        # Message d'erreur
        label_confirmation.config(text="Veuillez sélectionner un fichier.", fg="red")
        cheminimage = "pas de fichier"
#        return  # Arrête la fonction si aucun fichier n'est sélectionné

    # insertion dees données
    postid = db.insert_post(cheminimage, textepost, datepost)
    if postid:
        print("Insertion OK pour l'id : " + str(postid))
        # Message de confirmation
        label_confirmation.config(text="Données enregistrées avec succès !", fg="green")
    else:
        label_confirmation.config(text="Erreur d'enregistrement. Il y a déjà un texte pour cette date", fg="red")
        print("Pas d'insertion ! ")





# Chemin vers votre fichier .db
db = Database('Mes_Tweets.db')
print("BDD : Mes_Tweets.db" )

# Créer la fenêtre principale
fenetre = tk.Tk()
fenetre.title("Saisie de données")

style = ttk.Style()
style.theme_use('default')  # Utiliser le thème par défaut pour une base
style.configure('.', background='white', foreground='blue')  # Appliquer à tous les widgets
style.configure("TEntry", mask="##/##/####", foreground="blue", font=("Helvetica", 12))  # marche pas
style.configure("TButton", foreground="blue", font=("Helvetica", 12))

frame_saisie = ttk.Frame(fenetre, borderwidth=3, relief="solid")
frame_saisie.grid(row=0, column=0, padx=(20, 20), pady=(20, 0))

# Champs de saisie et boutons avec grid
label_date = ttk.Label(frame_saisie, text="Date de publication au format 01012024 :")
label_date.grid(row=0, column=0, sticky='w', pady=(20, 0))
entree_date = ttk.Entry(frame_saisie, style="TEntry")
entree_date.grid(row=0, column=1, sticky='w', pady=(20, 0))
entree_date.focus_set()

label_texte = ttk.Label(frame_saisie, text="Texte (280 caractères max) :")
label_texte.grid(row=1, column=0, sticky='w', pady=(20, 0))
entree_texte = tk.Text(frame_saisie, height=5, width=30)

entree_texte.grid(row=1, column=1, sticky='w', pady=(20, 0))

label_fichier = ttk.Label(frame_saisie, text="Sélectionner un fichier :")
label_fichier.grid(row=2, column=0, sticky='w', pady=(20))
entree_fichier = tk.Entry(frame_saisie, width=40)
entree_fichier.grid(row=2, column=1, sticky='w', pady=(20))

bouton_parcourir = ttk.Button(frame_saisie, text="Parcourir", command=parcourir_fichier)
bouton_parcourir.grid(row=2, column=2, sticky='w', padx=(20), pady=(20))

bouton_enregistrer = tk.Button(fenetre, text="Enregistrer", command=enregistrer_donnees)
bouton_enregistrer.grid(row=3, column=0, sticky='e', padx=(20), pady=(20))
#fenetre.bind('<Return>', lambda event: enregistrer_donnees())  # action de Entrée sur le bouton Enregistrer
# Problème : pas possible de saisir un retour à la ligne dans le champs de saisie du texte

# position du message d'erreur pas utilisé
label_erreur = tk.Label(fenetre, text="", fg="red")
label_erreur.grid(row=4, column=0, columnspan=3)

# message de confirmation
label_confirmation = tk.Label(fenetre, text="", fg="green")
label_confirmation.grid(row=4, column=0, columnspan=3)

fenetre.mainloop()

# lecture
"""
# Lecture en date du jour---a corriger
idPost, postStatut, lienImage, texteAPublier, daterecherche = db.lecture_post()
print(
    "Resultat en date du jour \nTexte = " + texteAPublier + "\n" + "Image = " + lienImage + "\n" + "Id du post = " + str(
        idPost) + "\nStatut = " + str(postStatut))

"""
db.close()
