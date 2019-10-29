import random

board = ['-','-','-',
        '-','-','-',
        '-','-','-']

options = ['tl','tm','tr',
          'ml', 'm','mr',
          'bl', 'bm', 'br']

counters = ['0', 'X']

first_move = ['y', 'n']

player_counter = ''
pc_counter = ''

print('\nxX0o NAUGHTS & CROSSES o0Xx')

mv_log = []

tkr = 0

pc = 0
player = 0
draw = 0

def choose_counter():
    global player_counter
    global pc_counter
    counter = input('Please select choice of counter: {}'.format(counters)).upper()
    while counter not in counters:
        counter = input('Invalid counter, please select choice of counter: {}'.format(counters)).upper()
    if counter == '0':
        player_counter = counters[0]
        pc_counter = counters[1]
    else:
        player_counter = counters[1]
        pc_counter = counters[0]

    return pc_counter

    print('your counter - {}\npc counter - {}'.format(player_counter, pc_counter))

def create_board():
    print('|' + board[0] + '|' + board[1] + '|' + board[2] + '|')
    print('|' + board[3] + '|' + board[4] + '|' + board[5] + '|')
    print('|' + board[6] + '|' + board[7] + '|' + board[8] + '|')

def player_move():

    player_move = input('\nYour move! available moves:\n{}\n'.format(options))

    while player_move not in options:
        player_move = input('Invalid move. Select again\n')

    while player_move in mv_log:
        player_move = input('Move already made. Select one of the following\n')

    if player_move == 'tl':
        board[0] = player_counter
    elif player_move == 'tm':
        board[1] = player_counter
    elif player_move == 'tr':
        board[2] = player_counter
    elif player_move == 'ml':
        board[3] = player_counter
    elif player_move == 'm':
        board[4] = player_counter
    elif player_move == 'mr':
        board[5] = player_counter
    elif player_move == 'bl':
        board[6] = player_counter
    elif player_move == 'bm':
        board[7] = player_counter
    else:
        board[8] = player_counter
    mv_log.append(player_move)
    options.remove(player_move)

def pc_move(pc_counter):
    print('\nPC move:\n')

    pc_move = random.choice(options)

    if pc_move == 'tl':
        board[0] = pc_counter
    elif pc_move == 'tm':
        board[1] = pc_counter
    elif pc_move == 'tr':
        board[2] = pc_counter
    elif pc_move == 'ml':
        board[3] = pc_counter
    elif pc_move == 'm':
        board[4] = pc_counter
    elif pc_move == 'mr':
        board[5] = pc_counter
    elif pc_move == 'bl':
        board[6] = pc_counter
    elif pc_move == 'bm':
        board[7] = pc_counter
    else:
        board[8] = pc_counter

    mv_log.append(pc_move)
    options.remove(pc_move)

def end_game():
    global tkr
    global player
    global pc
    global draw

    if board[0:3] == [player_counter, player_counter, player_counter]:
        tkr += 1
        player += 1
    elif board[3:6] == [player_counter, player_counter, player_counter]:
        tkr += 1
        player += 1
    elif board[6:9] == [player_counter, player_counter, player_counter]:
        tkr += 1
        player += 1
    elif board[0:7:3] == [player_counter, player_counter, player_counter]:
        tkr += 1
        player += 1
    elif board[1:8:3] == [player_counter, player_counter, player_counter]:
        tkr += 1
        player += 1
    elif board[2:9:3] == [player_counter, player_counter, player_counter]:
        tkr += 1
        player += 1
    elif board[2:7:2] == [player_counter, player_counter, player_counter]:
        tkr += 1
        player += 1
    elif board[0:9:4] == [player_counter, player_counter, player_counter]:
        tkr += 1
        player += 1
    elif board[0:3] == [pc_counter, pc_counter, pc_counter]:
        tkr += 2
        pc += 1
    elif board[3:6] == [pc_counter, pc_counter, pc_counter]:
        tkr += 2
        pc += 1
    elif board[6:9] == [pc_counter, pc_counter, pc_counter]:
        tkr += 2
        pc += 1
    elif board[0:7:3] == [pc_counter, pc_counter, pc_counter]:
        tkr += 2
        pc += 1
    elif board[1:8:3] == [pc_counter, pc_counter, pc_counter]:
        tkr += 2
        pc += 1
    elif board[2:9:3] == [pc_counter, pc_counter, pc_counter]:
        tkr += 2
        pc += 1
    elif board[2:7:2] == [pc_counter, pc_counter, pc_counter]:
        tkr += 2
        pc += 1
    elif board[0:9:4] == [pc_counter, pc_counter, pc_counter]:
        tkr += 2
        pc += 1
    elif '-' not in board:
        tkr = 3
        draw += 1
    else:
        tkr = 0

def refresh_board():

    global tkr

    tkr = 0

    global board

    board = ['-','-','-',
            '-','-','-',
            '-','-','-']

    global options

    options = ['tl','tm','tr',
              'ml', 'm','mr',
              'bl', 'bm', 'br']

    global mv_log
    mv_log = []

def play():
    choose_counter()
    first_move = input('Would you like to go first? Y/N').lower()
    while first_move not in first_move:
        first_move = input('Invalid selection, please select \'y\' or \'n\'')

    if first_move == 'y':
        while tkr == 0:
            create_board()
            player_move()
            end_game()
            if tkr != 0:
                break
            create_board()
            pc_move(pc_counter)
            end_game()
    else:
        while tkr == 0:
            create_board()
            pc_move()
            end_game()
            if tkr != 0:
                break
            create_board()
            player_move()
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

    print('SCOREBOARD: - Player:{} PC:{} Draw:{}'.format(player, pc, draw))

    while True:
        restart = input('Play again? y/n\n').lower()
        if restart == 'y':
            refresh_board()
            play()
        else:
            break

play()
