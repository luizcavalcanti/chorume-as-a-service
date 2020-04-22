import os
import twitter
from datetime import datetime

api = twitter.Api(
    consumer_key=os.environ["TWITTER_CONSUMER_KEY"],
    consumer_secret=os.environ["TWITTER_CONSUMER_SECRET"],
    access_token_key=os.environ["TWITTER_ACCESS_TOKEN"],
    access_token_secret=os.environ["TWITTER_TOKEN_SECRET"],
)

list_file = open("../README.md", "w")

header_file = open("./header", "r")
list_file.write(header_file.read())

blocks = api.GetBlocks()

list_file.write(
    f"\nLista exportada em: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}\n\n"
)

list_file.write(f"({len(blocks) } contas bloqueadas)\n\n")


list_file.write(
    "| Usuário | Criado em | Razão (Seguidores/Seguindo) | Tweets |\n"
    "| --- | --- | --- | --- |\n"
)

for user in blocks:
    user_image = f'![alt text]({user.profile_image_url} "foto do usuário")'
    user_url = f"https://twitter.com/{user.screen_name}"
    create_date = datetime.strptime(user.created_at, "%a %b %d %H:%M:%S %z %Y")
    follow_ratio = round(
        user.followers_count / user.friends_count if user.friends_count > 0 else 0.01, 3
    )

    list_file.write(
        f"| {user_image} [{user.name}]({user_url}) "
        f"| {create_date.strftime('%d/%m/%Y')} "
        f"| {follow_ratio} ({user.followers_count}/{user.friends_count}) "
        f"| {user.statuses_count} |\n"
    )

list_file.flush()
list_file.close()
