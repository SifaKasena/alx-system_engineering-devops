#!/usr/bin/python3
"""Get top ten posts for a subreddit"""
import requests


def top_ten(subreddit):
    """Get top ten posts for a subreddit"""
    url = f'https://www.reddit.com/r/{subreddit}/hot.json?limit=10'
    resp = requests.get(url, headers={'User-Agent': 'Scrape top_ten'})

    if resp.status_code != 200:
        print(None)
        return

    for post in resp.json()['data']['children']:
        print(post['data']['title'])
