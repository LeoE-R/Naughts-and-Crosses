import random

board = ['-','-','-',
        '-','-','-',
        '-','-','-']

options = ['tl','tm','tr',
          'ml', 'm','mr',
          'bl', 'bm', 'br']

cross = 'X'
naught = '0'

print('\nxX0o NAUGHTS & CROSSES o0Xx')

mv_log = []

tkr = 0

def create_board():
    print('|' + board[0] + '|' + board[1] + '|' + board[2] + '|')
    print('|' + board[3] + '|' + board[4] + '|' + board[5] + '|')
    print('|' + board[6] + '|' + board[7] + '|' + board[8] + '|')

def player_move():

    player_move = input('\nYour move! available moves:\n{}\n'.format(options))

    while player_move not in options:
        player_move = input('Invalid move. Select again')

    while player_move in mv_log:
        player_move = input('Move already made. Select again')

    if player_move == 'tl':
        board[0] = cross
    elif player_move == 'tm':
        board[1] = cross
    elif player_move == 'tr':
        board[2] = cross
    elif player_move == 'ml':
        board[3] = cross
    elif player_move == 'm':
        board[4] = cross
    elif player_move == 'mr':
        board[5] = cross
    elif player_move == 'bl':
        board[6] = cross
    elif player_move == 'bm':
        board[7] = cross
    else:
        board[8] = cross
    mv_log.append(player_move)
    options.remove(player_move)

def pc_move():
    print('\nPC move:\n')

    pc_move = random.choice(options)

    if pc_move == 'tl':
        board[0] = naught
    elif pc_move == 'tm':
        board[1] = naught
    elif pc_move == 'tr':
        board[2] = naught
    elif pc_move == 'ml':
        board[3] = naught
    elif pc_move == 'm':
        board[4] = naught
    elif pc_move == 'mr':
        board[5] = naught
    elif pc_move == 'bl':
        board[6] = naught
    elif pc_move == 'bm':
        board[7] = naught
    else:
        board[8] = naught

    options.remove(pc_move)

def end_game():
    global tkr

    if board[0:3] == ['X', 'X', 'X']:
        tkr += 1
    elif board[3:6] == ['X', 'X', 'X']:
        tkr += 1
    elif board[6:9] == ['X', 'X', 'X']:
        tkr += 1
    elif board[2:9:3] == ['X', 'X', 'X']:
        tkr += 1
    elif board[2:9:2] == ['X', 'X', 'X']:
        tkr += 1
    elif board[1:8:3] == ['X', 'X', 'X']:
        tkr += 1
    elif board[2:7:2] == ['X', 'X', 'X']:
        tkr += 1
    elif board[0:9:4] == ['X', 'X', 'X']:
        tkr += 1
    elif board[0:3] == ['0', '0', '0']:
        tkr += 2
    elif board[3:6] == ['0', '0', '0']:
        tkr += 2
    elif board[6:9] == ['0', '0', '0']:
        tkr += 2
    elif board[2:9:3] == ['0', '0', '0']:
        tkr += 2
    elif board[2:8:3] == ['0', '0', '0']:
        tkr += 2
    elif board[2:7:2] == ['0', '0', '0']:
        tkr += 2
    elif board[0:9:4] == ['0', '0', '0']:
        tkr += 2
    elif board[2:9:2] == ['0', '0', '0']:
        tkr += 2
    elif '-' not in board:
        tkr = 3
    else:
        tkr = 0

def play():

    while tkr == 0:
        create_board()
        player_move()
        end_game()
        if tkr != 0:
            break
        create_board()
        pc_move()
        end_game()

    if tkr == 1:
        create_board()
        print('\nYOU WIN! :^)')

    elif tkr == 2:
        create_board()
        print('\nPC WINS! :^(')

    else:
        create_board()
        print('\nDRAW! :^/')

play()
