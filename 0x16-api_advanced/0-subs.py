#!/usr/bin/python3
"""
Importing requests module
"""

from requests import get


def number_of_subscribers(subreddit):
    if subreddit is None or not isinstance(subreddit, str):
        return 0

    user_agent = {'User-agent': 'Google Chrome Version 81.0.4044.129'}
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)

    try:
        response = get(url, headers=user_agent)

        # Check if the request was successful
        if response.status_code == 200:
            all_data = response.json()
            return all_data.get('data').get('subscribers')
        else:
            print("Error: Unable to fetch data. Status Code:", response.status_code)

    except Exception as e:
        print("Error:", str(e))

    return 0
