# B Simpson

# TODO write bash script that ensures pychord is on the server and call it here

import sys

from pychord import Chord
from typing import *

def build_chord():
    raise NotImplementedError

def welcome_user() -> None:
    """Welcomes the user to the program.
    """
    welcomeMessage = 'Welcome to Lyra!'
    instructions = 'Please type a comma separated list of chords ending with' \
        ' a period (.) and press ENTER.\n(e.g. Cm,A#M7,BbM9,F#M9.)'
    
    print(' ' + '-' * int(len(welcomeMessage) + 4))
    print('/ {} /'.format(welcomeMessage))
    print('-' * int(len(welcomeMessage) + 4))
    print('{}\n'.format(instructions))

    return None

def get_chord_progression() -> List[str]:
    """
    """
    userInput = input()
    
    while userInput[-1] != '.':
        print('Oops! Make sure to include a period (.) at the end.')
        sys.stdout.flush()
        userInput = input()
    # remove the trailing period
    userInput = userInput[:-1]
    # remove all whitespace for each entry
    chordProgression = [''.join(s.strip()) for s in userInput.split(',')]

    return chordProgression

def main():
    
    welcome_user()
    chordComponentList = []
    chordProgression = get_chord_progression()
    
    for chord in chordProgression:
            try:
                chordComponentList.append(Chord(chord).components())
            except Exception as ex:
                print('Error: {}. Omitting chord {} in progression'.format(ex, chord))
    print(chordComponentList)
    return

if __name__ == '__main__':
    main()
