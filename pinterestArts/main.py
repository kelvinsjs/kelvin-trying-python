from py3pin.Pinterest import Pinterest

pinterest = Pinterest(email='grishakelvin@gmail.com',
                      password='8r5F5hUBxuge7dJV',
                      username='grigorijostapenko')
pinterest.login()
user_profile = pinterest.get_user_overview()


def getBoardIds(username):
    dictBoards = {}
    boards = pinterest.boards(username=username)
    for board in boards:
        dictBoards[board['name']] = board['id']
    return dictBoards

def get_boards(username='grishakelvin'):
    return pinterest.boards_all(username=username)

def fuckingFuck(board_id):
    board_feed = []
    feed_batch = pinterest.board_feed(board_id=board_id)
    while len(feed_batch) > 0:
        board_feed += feed_batch
        feed_batch = pinterest.board_feed(board_id=board_id)
    count_pins = len(board_feed)
    return count_pins

print(fuckingFuck(576460958462043383))


