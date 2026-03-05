import time
import requests

# Strict rate limit enforcement: 1 request per 10 seconds
RATE_LIMIT_DELAY = 10 

def fetch_subreddit_hot(subreddit_name, headers):
    url = f"https://oauth.reddit.com/r/{subreddit_name}/hot"
    response = requests.get(url, headers=headers)
    
    # Mandatory sleep to comply with API rules
    time.sleep(RATE_LIMIT_DELAY)
    
    return response.json()

# Note: Data is processed locally and discarded. No database storage. No ML training.
