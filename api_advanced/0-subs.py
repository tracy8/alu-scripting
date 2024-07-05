#!/usr/bin/python3
"""DOCUMENTING"""
import requests


def number_of_subscribers(subreddit):
    """DOC"""
    reddit_url = "https://www.reddit.com/r/{}/about.json".format(subreddit)

    header = {'User-agent': 'Mozilla/5.0'}
    response = requests.get(reddit_url,
                            headers=header
                            )

    if response.status_code == 200:
        data = response.json()['data']
        subs = data['subscribers']
        return subs
    return 0
print(number_of_subscribers("programming"))
