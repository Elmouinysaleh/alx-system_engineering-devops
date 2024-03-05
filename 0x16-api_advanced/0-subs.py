#!/usr/bin/python3
"""Function to query subscribers on a given Reddit subreddit."""
import requests
import sys

def number_of_subscribers(subreddit):
    """Return the total number of subscribers on a given subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"}
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        response.raise_for_status()  # Raise an exception for 4xx and 5xx status codes
        data = response.json()
        if "data" in data and "subscribers" in data["data"]:
            return data["data"]["subscribers"]
        else:
            print(f"Error: Unexpected JSON format. Response content: {response.content}")
            return 0
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return 0
