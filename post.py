
import tweepy


bearer_token = "AAAAAAAAAAAAAAAAAAAAAOt5vwEAAAAAAq8xJOXUcxJHsSmkSzX5y53SeGU%3DuZCfaaJNPIgDcCxVqTHVFGI0Qf1WftnJeKyPR75QISzaxYM4hI"
api_key ="0DkVrPkPRWjhQCIgyR9ddQwvX"
api_secret_key = "BHBA1w1qb8ZYrTOBp3TJ1hTt4tGOGnPuxNTaDgXfs8b1Y4lKfz"
access_token = "1834514755572117504-saox09HARQwKcjiFPZdlC7DvlR2B19"
access_token_secret = "ZGVTlkcDSgmZgRfs3IpXmAxQFL4tnKO5rvDNk7xqPR06h"

#auth = tweepy.OAuth2BearerHandler(bearer_token)
client = tweepy.Client(bearer_token, api_key,api_secret_key,access_token,access_token_secret)

#TWEET fait autentification OK"


tweet = "Tester encore et encore"
response = client.create_tweet(text=tweet)
#Response(data={'edit_history_tweet_ids': ['1855316226970415587'], 'id': '1855316226970415587', 'text': 'Deuxième test pour voir la réponse'}, includes={}, errors=[], meta={})
print("Tweet posted successfully!", response)
#Response(data={'text': 'Tester encore et encore', 'id': '1857796667879125144', 'edit_history_tweet_ids': ['1857796667879125144']}, includes={}, errors=[], meta={})
