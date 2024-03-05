#!/usr/bin/python3
"""
Module to query the Reddit API and get the number of subscribers for a subreddit
"""
import requests

def number_of_subscribers(subreddit):
    """
    Function to get the number of subscribers for a subreddit

    Args:
        subreddit (str): The name of the subreddit

    Returns:
        int: Number of subscribers for the subreddit, 0 if invalid subreddit
    """
    # Set a custom User-Agent to avoid issues
    headers = {'User-Agent': 'MyRedditBot/1.0 (by YourUsername)'}

    # Make a request to the Reddit API
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    response = requests.get(url, headers=headers, allow_redirects=False)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON response and return the number of subscribers
        data = response.json()
        subscribers = data['data']['subscribers']
        return subscribers
    elif response.status_code == 404:
        # Subreddit not found, return 0
        return 0
    else:
        # Handle other errors
        print(f"Error: {response.status_code}")
        return 0

if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        subreddit_name = sys.argv[1]
        subscribers_count = number_of_subscribers(subreddit_name)
        print("{:d}".format(subscribers_count))
