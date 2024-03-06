#!/usr/bin/python3
"""
Importing requests module
"""

import requests

def number_of_subscribers(subreddit):
    if subreddit is None or not isinstance(subreddit, str):
        return 0

    user_agent = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:97.0) Gecko/20100101 Firefox/97.0'}
    url = f'https://www.reddit.com/r/{subreddit}/about.json'

    try:
        response = requests.get(url, headers=user_agent)

        # Check if the request was successful
        if response.status_code == 200:
            all_data = response.json()
            return all_data.get('data').get('subscribers')
        else:
            print("Error: Unable to fetch data. Status Code:", response.status_code)

    except Exception as e:
        print("Error:", str(e))

    return 0
