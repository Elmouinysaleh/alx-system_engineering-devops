#!/usr/bin/python3
"""Function to query subscribers on a given Reddit subreddit."""
import requests

def number_of_subscribers(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        if 'data' in data and 'subscribers' in data['data']:
            subscribers = data['data']['subscribers']
            return subscribers

    return 0
