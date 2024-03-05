#!/usr/bin/python3
"""Function to query subscribers on a given Reddit subreddit."""
import requests

def number_of_subscribers(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "My Reddit API Client"}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an exception for any HTTP errors
        data = response.json()
        subscribers = data["data"]["subscribers"]
        return subscribers
    except requests.exceptions.RequestException as e:
        print(f"Error occurred: {e}")
        return 0
