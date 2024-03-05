#!/usr/bin/python3
"""
1-Top_ten hot posts listed for a given subreddit.
"""


import requests

def top_ten(subreddit):
    # Set custom User-Agent to avoid throttling
    headers = {'User-Agent': 'my_custom_user_agent'}

    # Construct the URL without following redirects
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"  # Limit=10 for first 10 posts
    response = requests.get(url, headers=headers, allow_redirects=False)

    # Check for successful response (200 OK) or redirection (302 Found)
    if response.status_code == 200:
        data = response.json()
        posts = data.get('data', {}).get('children', [])
        if not posts:
            print("No posts found.")
        else:
            for post in posts:
                print(post['data']['title'])
    else:
        print("None")  # Handle unsuccessful response or invalid subreddit
