#!/usr/bin/env python3
'''
    File name: config.py
    Author: Benjamin Simpson
    Date created: 2/23/2017
    Date last modified: 4/17/2019
    Python Version: 3.6.8
'''

# TODO write bash script that ensures pychord is on the server and call it here

# python modules
import sys
from typing import *

# third party modules
from pychord import Chord


def build_chord():
    raise NotImplementedError

def print_welcome_msg() -> None:
    """Welcomes the user to the program.
    """
    welcomeMessage = 'Welcome to Lyra!'
    instructions = 'Please type a comma separated list of chords ending with' \
        ' a period (.) and press ENTER.\n(e.g. Cm,A#M7,BbM9,F#M9.)' \
        '\nTo quit, type q and press ENTER.'
    
    print(' ' + '-' * int(len(welcomeMessage) + 4))
    print('/ {} /'.format(welcomeMessage))
    print('-' * int(len(welcomeMessage) + 4))
    print('{}\n'.format(instructions))

    return None

def get_chord_progression() -> List[str]:
    """Calls for user input and returns a list of chords.
    """
    userInput = input()
    
    while userInput[-1] != '.':
        if userInput == 'q':
            print('~ Goodbye! ~')
            sys.exit()
        print('Oops! Make sure to include a period (.) at the end.')
        sys.stdout.flush()
        userInput = input()
    # remove the trailing period
    userInput = userInput[:-1]
    # remove all whitespace for each entry
    chordProgression = [''.join(s.strip()) for s in userInput.split(',')]

    return chordProgression

def main():
    
    print_welcome_msg()
    chordComponentList = []
    chordProgression = get_chord_progression()
    
    for chord in chordProgression:
            try:
                chordComponentList.append(Chord(chord).components())
            except Exception as ex:
                print('Error: {}. Omitting chord {} in progression'.format(ex, chord))
    print('Constiutent notes of chords entered: {}'.format(chordComponentList))
    return

if __name__ == '__main__':
    main()
