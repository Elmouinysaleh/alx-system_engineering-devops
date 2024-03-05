#!/usr/bin/python3
"""Function to query subscribers on a given Reddit subreddit."""
import requests

def number_of_subscribers(subreddit):
  """Queries Reddit API for subscriber count (unofficial).

  Args:
      subreddit: The name of the subreddit (e.g., "programming").

  Returns:
      An integer representing the subscriber count (approximate), 
      or 0 if the subreddit is invalid.
  """
  # Set custom User-Agent to avoid throttling
  headers = {'User-Agent': 'my_custom_user_agent'}

  # Construct the URL without following redirects
  url = f"https://www.reddit.com/r/{subreddit}/about.json?limit=0"  # Limit=0 avoids extra data
  response = requests.get(url, headers=headers, allow_redirects=False)

  # Check for successful response (200 OK)
      if response.status_code == 200:
    data = response.json()
    # Extract subscriber count from data (may vary based on API updates)
         return data.get('data', {}).get('subscribers', 0)
      else:
    # Handle unsuccessful response or invalid subreddit
         return 0
