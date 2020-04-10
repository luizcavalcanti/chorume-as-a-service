import os
import twitter
import datetime

api = twitter.Api(
    consumer_key=os.environ["TWITTER_CONSUMER_KEY"],
    consumer_secret=os.environ["TWITTER_CONSUMER_SECRET"],
    access_token_key=os.environ["TWITTER_ACCESS_TOKEN"],
    access_token_secret=os.environ["TWITTER_TOKEN_SECRET"],
)

blocks = api.GetBlocks()

header = "# chorume-as-a-service\nLista de gente e robô muito bosta no twitter\n---\n| Foto | Usuário | Seguidores | Seguindo | Criado em |\n| --- | --- | --- | --- | --- |\n"

list_file = open("../README.md", "w")

list_file.write(header)

for user in blocks:
    user_image = f'![alt text]({user.profile_image_url} "foto do usuário")'
    user_url = f"https://twitter.com/{user.screen_name}"
    create_date = datetime.datetime.strptime(user.created_at, "%a %b %d %H:%M:%S %z %Y")

    list_file.write(
        f"| {user_image} | [{user.name}]({user_url}) | {user.followers_count} | {user.friends_count} | {create_date.strftime('%d/%m/%Y')} |\n"
    )

now = datetime.datetime.now()

list_file.write(f"\n---\nLista exportada em: {now.strftime('%d/%m/%Y %H:%M:%S')}\n")

list_file.flush()
list_file.close()
