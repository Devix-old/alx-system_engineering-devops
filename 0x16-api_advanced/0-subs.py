#!/usr/bin/python3
"""Retrieve the number of subscribers of a subreddit on
Reddit using the API."""

import requests


def number_of_subscribers(subreddit):
    """Return the number of subscribers for a subreddit."""
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) Apple' +
        'WebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'
    }
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()['data']['subscribers']
    else:
        return 0
