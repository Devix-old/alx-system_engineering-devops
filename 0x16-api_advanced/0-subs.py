#!/usr/bin/python3
"""Retrieve the number of subscribers of a subreddit on
Reddit using the API."""
import requests


def number_of_subscribers(subreddit):
    """Return the number of subscribers for a subreddit."""
    headers = {'user-agent': 'request'}
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    response = requests.get(url, headers=headers, allow_redirects=None)
    if response.status_code != 200:
        return 0
    data = response.json().get("data")
    subs = data.get("subscribers")
    return subs
