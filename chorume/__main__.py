import os
import sys

import twitter

from . import export, block


def _init_api():
    return twitter.Api(
        consumer_key=os.environ["TWITTER_CONSUMER_KEY"],
        consumer_secret=os.environ["TWITTER_CONSUMER_SECRET"],
        access_token_key=os.environ["TWITTER_ACCESS_TOKEN"],
        access_token_secret=os.environ["TWITTER_TOKEN_SECRET"],
    )


if __name__ == "__main__":
    twitter_api = _init_api()
    command = sys.argv[1]
    if command == "export":
        export.export_blocked_users(twitter_api)
    elif command == "block":
        block.block_users(twitter_api)
    else:
        print(f"Command %s not found" % sys.argv[1])
