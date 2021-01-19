import csv

LINE_CLEARER = 20 * ' '


def _read_export_csv(file_name):
    with open(file_name, 'r') as file:
        blocks = [line for line in csv.DictReader(file)]
        return blocks


def block_users(twitter_api):
    blocks = _read_export_csv('blocks.csv')
    total_blocks = len(blocks)
    blocked = 0

    print("\nThere are %d ARROMBADINHOS to block.\nPlease hang in there!\n\n" % len(blocks))

    for user in blocks:
        blocked += 1
        print(f'\r[%d of %d] Blocking %s...%s' % (blocked, total_blocks, user['screen_name'], LINE_CLEARER), end='')
        twitter_api.CreateBlock(user_id=user['user_id'])

    print()
    print("Done :)")
