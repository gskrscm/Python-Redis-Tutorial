import redis
import requests
import json

redis = redis.Redis()


def get_github_profile(username):
    # Read from cache, otherwise fetch
    result = redis.get(username)

    if not result:
        fetch_github_profile(username)
    else:
        # Remember to convert to string, redis values are stored as bytes
        print(
            json.dumps({
                "cached": True,
                "profile": str(result)
            })
        )


def fetch_github_profile(username):
    # Get the result from Github and cache it
    result = requests.get("https://api.github.com/users/" + username)

    redis.setex(username, 10, str(result.json()))

    print(
        json.dumps({
            "cached": False,
            "profile": result.json()
        })
    )


get_github_profile("taimoorgit")
