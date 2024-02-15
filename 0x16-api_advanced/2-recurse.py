import requests

"""A module for fetching titles from the hot section of a subreddit."""


def recurse(subreddit, hot_list=[], after=None):
    """Recursively fetches titles from the hot section of a subreddit.
    """

    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) Apple' +
        'WebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'
    }

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    params = {'after': after} if after else {}
    response = requests.get(url, params=params, headers=headers, allow_redirects=None)

    if response.status_code == 200:
        data = response.json()
        posts = data['data']['children']
        for post in posts:
            hot_list.append(post['data']['title'])

        after = data['data'].get('after')
        if after:
            return recurse(subreddit, hot_list, after)
        else:
            return hot_list if hot_list else None
    else:
        return None
