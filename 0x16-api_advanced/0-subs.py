#!/usr/bin/python3
"""Retrieve the number of subscribers of a subreddit on
Reddit using the API."""
import requests


def number_of_subscribers(subreddit):
    """Return the number of subscribers for a subreddit."""
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.3'}
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    response = requests.get(url, headers=headers, allow_redirects=None)
    if response.status_code != 200:
        return 0
    data = response.json().get("data")
    subs = data.get("subscribers")
    return subs
