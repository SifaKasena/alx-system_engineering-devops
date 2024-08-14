#!/usr/bin/python3
"""Returns the number of subscribers for a given subreddit"""
import requests


def number_of_subscribers(subreddit):
    """Returns the number of subscribers for a given subreddit"""
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    resp = requests.get(url, headers={'User-Agent': 'Scrape subsribers'})

    if resp.status_code != 200:
        return (0)

    return (resp.json()['data']['subscribers'])
