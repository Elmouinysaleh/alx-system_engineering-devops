#!/usr/bin/python4
"""
Function to query subscribers on a given Reddit subreddit.
"""
import requests

def number_of_subscribers(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        if 'kind' in data and data['kind'] == 't5':
            subscribers = data['data']['subscribers']
            return subscribers

    return 0
