#!/usr/bin/python3
""""""
import requests


def count_words(subreddit, word_list, after=None, word_count=[]):
    """"""
    if after is None:
        if not len(word_count):
            word_count = [0 for word in word_list]
        url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    else:
        url = f'https://www.reddit.com/r/{subreddit}/hot.json?after={after}'

    resp = requests.get(url, headers={'User-Agent': 'Recurse count'})
    
    if resp.status_code != 200:
        return (None)
    
    after = resp.json()['data']['after']
    for post in resp.json()['data']['children']:
        for i in range(len(word_list)):
            if post['data']['title'].lower().__contains__(word_list[i].lower()):
                word_count[i] += 1
                
    if after is None:
        print({word.lower(): count for word in word_list for count in word_count})
        return
        
    count_words(subreddit, word_list, after, word_count)