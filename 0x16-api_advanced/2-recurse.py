#!/usr/bin/python3
"""Returns a list of all hot articles"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """Returns a list of all hot articles"""
    if after is None:
        url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    else:
        url = f'https://www.reddit.com/r/{subreddit}/hot.json?after={after}'

    resp = requests.get(url, headers={'User-Agent': 'Recurse hot'})

    if resp.status_code != 200:
        return (None)

    after = resp.json()['data']['after']
    for post in resp.json()['data']['children']:
        hot_list.append(post['data']['title'])

    if after is None:
        return (hot_list)

    return (recurse(subreddit, hot_list, after))
