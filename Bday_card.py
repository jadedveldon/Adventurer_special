import os, shutil, sys, time
yes = ['yes', 'Yes', 'y', 'Y']
no = ['No', 'no', 'n', 'N']
def typewriter(message):
    for char in message:
        sys.stdout.write(char)
        sys.stdout.flush()
        
        if char != '\n':
            time.sleep(0.08)
        else:
            time.sleep(0.8)

def guard_convo():
    guard_play = False
    while guard_play is False:
        typewriter('''
~~~ By the entrance of the majestic, but shut, stone door, a guard quietly and
methodically sharpens his knife.

As you get closer the young man lifts his cold, brown eyes and with them
touches your soul.

He measures you for a brief moment, then starts back on his blade.
''')
        talk_to_guard = input('\n~~~ Talk to the guard? ')
        if talk_to_guard in yes:
            typewriter('''
"You have come a long way Saumya... if that is really you.
 How long has it been? More than a thousand years at least.
 If you truly are my old friend, none other than the grinning witch, you will know
 what this means..."

The young man points at a mysterious carving on top the old door...
''')
            game_start = input('\n~~~ Decypher the carving? clue: its a special name given to the witch ')
            if game_start in yes:
                guard_play = True          
            else: 
                guard_play = False

def hangman():
    underscore = '_ '
    secret_word = 'gilheri'

    secret_lst = list(secret_word)

    under_lst = []
    for element in secret_lst:
        under_lst.append('_ ')

    # visual representation: '_ _ _ _ _ _' 
    under_word = ' '.join(under_lst)

    new_lst = under_lst

    while underscore in new_lst:         
        clean_new_lst = ' '.join(new_lst) # constantly updated visual rep (is a string)
        
        columns = shutil.get_terminal_size().columns # center visual rep
        print()
        print(clean_new_lst.center(columns))
        
        guess = input('\nTake a guess, one letter at a time: ' )
        for element in range(len(secret_lst)):
            if guess == secret_lst[element]:
                new_lst[element] = secret_lst[element]
            else:
                continue

def manuscript(): 
    to_read = False
    while to_read is False:
        typewriter('''
The heavy door slowly opens as the guard slyly smiles at you. You nod at him and
hastly make your way inside.

Although you know you're safe and will defend yourself if you must, you're happy to
move past him. Something about him...

Your first steps into the cave-room echo throughout it.
The candles looming from the ceiling draw your eyes straight ahead onto an altar on
the opposite end of the room.

You make your way towards it...

Next to a lone candle (how long has it been burning?), a rolled parchment lays idle
on top of the altar.

You pick it up, turn it around and inspect the seal.
It reads:

                             'SAUMYA'\n
''')
        read = input('Break the seal and read the parchment? ')
        if read in yes:
            to_read = True
        else:
            to_read = False


# END OR PLAY AGAIN?
def end_of_game():
    play_again = input('\n>>> Play again? ')
    if play_again in yes:
        return
    elif play_again in no:
        print('\nUntil next time...\n')
    exit()


# ---------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------
  
  
# MAIN GAME
while True:
    # start game
    guard_convo()
        
    # hangman mini-game
    hangman()
    
    # cave action
    manuscript()
    
    # manuscript
    exec(open("Letter.py").read()) # prints the letter I wrote
    
    # cake
    exec(open("Bday_Ascii.py").read()) # prints the artwork
    
    # pause
    time.sleep(2)
    
    # exit or play again?
    end_of_game()
  
