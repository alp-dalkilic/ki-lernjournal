def uebung_1(): #while loop mit continue und break
    while True:
        print('Who are you?')
        name = input('>')

        if name != 'Joe':
            continue

        print('Hello, Joe. What is the password?')
        password = input('>')

        if password == 'swordfish':
            break

    print('Access granted.')


def uebung_2(): # Five Times - 'for' and 'range' function
    print('Hello!')
    for i in range(5):
        print('On this iteration, i is set to ' + str(i))
    print('Goodbye!')

def uebung_3():
    total = 0
    for num in range(101):
        total = total + num
    print(total)

def uebung_4():# Game rock, paper, scissor

    import random, sys
    print('ROCK, PAPER, SCISSORS')
    # These variables keep track of the number of wins, losses, and ties.
    wins = 0
    losses = 0
    ties = 0
    while True: # The main game loop
        print('%s Wins, %s Losses, %s Ties' % (wins, losses, ties))
        while True: # The player input loop
            print('Enter your move: (r)ock (p)aper (s)cissors or (q)uit')
            player_move = input('>')
            if player_move == 'q':
                sys.exit() # Quit the program.
            if player_move == 'r' or player_move == 'p' or player_move == 's':
                break # Break out of the player input loop.
            print('Type one of r, p, s, or q.')
    # Display what the player chose:
        if player_move == 'r':
            print('ROCK versus...')
        elif player_move == 'p':
            print('PAPER versus...')
        elif player_move == 's':
            print('SCISSORS versus...')
    # Display what the computer chose:
        move_number = random.randint(1, 3)
        if move_number == 1:
            computer_move = 'r'
            print('ROCK')
        elif move_number == 2:
            computer_move = 'p'
            print('PAPER')
        elif move_number == 3:
            computer_move = 's'
            print('SCISSORS')
    # Display and record the win/loss/tie:
        if player_move == computer_move:
            print('It is a tie!')
            ties = ties + 1
        elif player_move == 'r' and computer_move == 's':
            print('You win!')
            wins = wins + 1
        elif player_move == 'p' and computer_move == 'r':
            print('You win!')
            wins = wins + 1
        elif player_move == 's' and computer_move == 'p':
            print('You win!')
            wins = wins + 1
        elif player_move == 'r' and computer_move == 'p':
            print('You lose!')
            losses = losses + 1
        elif player_move == 'p' and computer_move == 's':
            print('You lose!')
            losses = losses + 1
        elif player_move == 's' and computer_move == 'r':
            print('You lose!')
            losses = losses + 1


def uebung_5(): # lists, slice [:] and index [1,4] = 1 bis 3 letzter Wert nicht enthalten
    spam = ['cat', 'bat', 'rat', 'elephant']
    print(spam[-2]) #Erwartet rat
    print(spam[1:3]) #Erwartet bat, rat
    print(spam[:]) #Gesamte Liste
    print(spam[:2]) #Erwartet cat, bat
    print(spam[2:]) #Erwartet rat, elephant

def uebung_6():
    # value updates
    spam = ['Nora', 'Xenia', 'Alp', 'Mimi']
    print(spam[:]) # Erwartet komplete LIst
    spam[3] = 'lieber ohne Mimi'
    print(spam[:]) # Erwartet kompletet List ohne Mimi
    spam[0] = spam[1]
    print(spam[:]) # Erwartet zweimal Xenia ohne Mimi
    spam[2] = spam[3]
    print(spam[:]) # Erwartet zweimal Xeni, zweimal 'Lieber ohne Mimi'

uebung_6()
