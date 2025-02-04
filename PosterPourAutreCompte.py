import tweepy
bearer_token = "AAAAAAAAAAAAAAAAAAAAAOt5vwEAAAAAAq8xJOXUcxJHsSmkSzX5y53SeGU%3DuZCfaaJNPIgDcCxVqTHVFGI0Qf1WftnJeKyPR75QISzaxYM4hI"
api_key ="0DkVrPkPRWjhQCIgyR9ddQwvX"
api_secret_key = "BHBA1w1qb8ZYrTOBp3TJ1hTt4tGOGnPuxNTaDgXfs8b1Y4lKfz"

access_token = "1834514755572117504-saox09HARQwKcjiFPZdlC7DvlR2B19"
access_token_secret = "ZGVTlkcDSgmZgRfs3IpXmAxQFL4tnKO5rvDNk7xqPR06h"

consumer_key = 'bXVFMEFFcTNNakFNYUkxVXZ4T1Y6MTpjaQ'
consumer_secret = 'eNTnyxVlDpKih0IgPUhjl8Yzw1Ven3B56eQ5jyFruiqMtB9VqO'

# Remplacer par les clés d'accès de l'utilisateur
auth = tweepy.OAuth1UserHandler(
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)
try:
    api = tweepy.API(auth)

    # Publier un tweet
    api.update_status("Mon nouveau tweet depuis un autre compte !")
    print("post ok")
except Exception as e:
    print("Une erreur s'est produite : " + str(e))