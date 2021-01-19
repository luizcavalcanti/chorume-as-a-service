import csv
import os
from datetime import datetime

import twitter


def _export_markdown(blocks, file_name):
    with open(file_name, 'w') as list_file:
        header_file = open("templates/markdown_header", "r")
        list_file.write(header_file.read())

        list_file.write(f"\n\n")
        list_file.write(
            f"\n({len(blocks)} contas bloqueadas em {datetime.now().strftime('%d/%m/%Y %H:%M:%S')})\n\n"
        )
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


def _export_simple_csv(blocks, file_name):
    csv_columns = ['user_id', 'screen_name']
    dict_data = [{'id': user.id, 'name': user.screen_name} for user in blocks]
    with open(file_name, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
        writer.writeheader()
        for data in dict_data:
            writer.writerow(data)


def export():
    api = twitter.Api(
        consumer_key=os.environ["TWITTER_CONSUMER_KEY"],
        consumer_secret=os.environ["TWITTER_CONSUMER_SECRET"],
        access_token_key=os.environ["TWITTER_ACCESS_TOKEN"],
        access_token_secret=os.environ["TWITTER_TOKEN_SECRET"],
    )
    blocks = api.GetBlocks()

    _export_markdown(blocks, 'README.md')
    _export_simple_csv(blocks, 'blocks.csv')
