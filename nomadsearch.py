import requests
import json
import datetime

# Set the search query
query = "Hashicorp Nomad"

# Set the headers with the bearer token
headers = {
    "Authorization": "Bearer <YOUR BEARER TOKEN FROM TWITTER DEV TOOLS>"
}

# Get the current date and time
now = datetime.datetime.now()

# Set the start and end dates for the search
start_time = (now - datetime.timedelta(days=1)).strftime("%Y-%m-%dT%H:%M:%SZ")
end_time = now.strftime("%Y-%m-%dT%H:%M:%SZ")

# Request tweets from the Twitter Search API
response = requests.get(f"https://api.twitter.com/2/tweets/search/recent?query={query}&start_time={start_time}&end_time={end_time}", headers=headers)

if response.status_code == 200:
    # Get the JSON data from the response
    data = response.json()
    # Open a file for writing
    with open("nomad_tweets.txt", "w") as f:
        for tweet in data["data"]:
            # Write the text of the tweet to the file
            # create a link to map to tweet id
            twitter_link="https://twitter.com/anyuser/status/" + tweet["id"]
            twitter_text=tweet["text"]
            f.write(twitter_link + "\n" + "\n")
            f.write(twitter_text + "\n")
    print("Tweets saved to nomad_tweets.txt")
else:
    print(f"Error {response.status_code}: {response.text}")
