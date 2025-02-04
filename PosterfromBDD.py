import tweepy
#BlueSky
from atproto import Client

from gestionBDD import Database



#Bluesky
def poster_bluesky(texte):
    clientbs = Client()
    try:
        clientbs.login('tinadarnoux.bsky.social', 'Cultura2023.')
        clientbs.send_post(texte)
        postbsok = True
        return postbsok
    except Exception as e:
        print("Une erreur s'est produite !bs: " + str(e))


def poster_tweet_avec_image(image_path, texte):
    # twitter
    bearer_token = "AAAAAAAAAAAAAAAAAAAAAOt5vwEAAAAAAq8xJOXUcxJHsSmkSzX5y53SeGU%3DuZCfaaJNPIgDcCxVqTHVFGI0Qf1WftnJeKyPR75QISzaxYM4hI"
    api_key = "0DkVrPkPRWjhQCIgyR9ddQwvX"
    api_secret_key = "BHBA1w1qb8ZYrTOBp3TJ1hTt4tGOGnPuxNTaDgXfs8b1Y4lKfz"
    access_token = "1834514755572117504-saox09HARQwKcjiFPZdlC7DvlR2B19"
    access_token_secret = "ZGVTlkcDSgmZgRfs3IpXmAxQFL4tnKO5rvDNk7xqPR06h"

    # auth = tweepy.OAuth2BearerHandler(bearer_token)
    client = tweepy.Client(bearer_token, api_key, api_secret_key, access_token, access_token_secret)
    try:
        # KO sur l'image client.create_tweet(text=texte, media_ids=image_path    )
        client.create_tweet(text=texte)
        posttwitterok = True
        print("Tweet publié avec succès !")
        return posttwitterok
    except Exception as e:
        print("Une erreur s'est produite : " + str(e))


# Chemin vers votre fichier .db
db = Database('Mes_Tweets.db')
print("BDD : Mes_Tweets.db")
# lecture

# Lecture en date du jour
try:
    idPost, postStatut, lienImage, texteAPublier, daterecherche = db.lecture_post()
    if idPost == 0:
        print("Pas de post")
    else:
        print(
            "Resultat en date du jour \nTexte = " + texteAPublier + "\n" + "Image = " + lienImage + "\n" + "Id du post = " + str(
                idPost) + "\nStatut = " + str(postStatut))
        # Post

        postTWOK = poster_tweet_avec_image(lienImage, texteAPublier)
        postBSOK = poster_bluesky(texteAPublier)
#        postTWOK = True
#        postBSOK = True
        if postTWOK & postBSOK:
            print("maj bdd à faire")
            postvalide = db.update(idPost)
        else:
            print("Post KO pas de maj. Post Twitter : " + postTWOK + "POST BS : " + postBSOK )
except ValueError:
    print("Problème de récupération du texte")

db.close()
