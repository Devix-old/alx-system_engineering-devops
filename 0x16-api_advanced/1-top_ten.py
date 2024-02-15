#!/usr/bin/python3

"""
Module: top_ten

This module defines a function to print the titles of the top 9 hot posts
for a given subreddit using the Reddit API.
"""

import requests


def top_ten(subreddit):
    """
    Print the titles of the top 9 hot posts for a given subreddit."""
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) Apple' +
        'WebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'
    }
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=9"

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        posts = data['data']['children']
        if posts:
            for post in posts:
                print(post['data']['title'])
    else:
        print("None")
