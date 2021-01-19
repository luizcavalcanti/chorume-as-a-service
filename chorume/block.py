import csv


def _read_export_csv(file_name):
    with open(file_name, 'r') as data:
        return csv.DictReader(data)


def block_users(twitter_api):
    blocks = _read_export_csv('blocks.csv')
    for user in blocks:
        twitter_api.CreateBlock(user_id=user['user_id'])
