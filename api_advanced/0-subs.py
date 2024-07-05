#!/usr/bin/python3
"""
Returns the number of subscribers from a subreddit
"""
import requests

def number_of_subscribers(subreddit):
    """Queries the Reddit API and returns the number of subscribers"""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "ALU-scripting API 0.1"}

    try:
        response = requests.get(url, headers=headers, timeout=10, allow_redirects=False)
        if response.status_code == 200:
            data = response.json().get("data", {})
            return data.get("subscribers", 0)
        else:
            return 0
    except requests.RequestException:
        return 0
