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
import pychord as pc

class Lyra:
    def __init__(self):
        self.tuningIndices = [4, 9, 2, 7, 11, 4]
        pass
        
    def chord_to_guitar(self, chordObj) -> List[Tuple[int]]:
        """
        """
        # NOTE notes in pychord stored [C, C#, D, D#, E, F, F#, G, G# A, A#, B]
        chordIndices = chordObj.components(visible=False)
        # NOTE for C, this is [0, 4, 7]
        for ci in chordIndices:
            # generate every viable fret for this chord note index
            for gs in self.tuningIndices:
                fret = (ci - gs) % 12
                print('Chord index: {}, string: {}, fret: {}'.format(ci, gs, fret)) 
        return

    def print_welcome_msg(self) -> None:
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

    def get_user_chord_progression(self) -> List:
        """Calls for user input and returns a list of chord objects.
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
        chordProgression = [pc.Chord(''.join(s.strip())) for s in userInput.split(',')]

        return chordProgression

def main():
    lyra = Lyra()
    lyra.print_welcome_msg()
    
    try:
        chordProgression = lyra.get_user_chord_progression()            
    except Exception as ex:
        print('Error: {}. Omitting chord {} in progression'.format(ex, chord))
    
    for chord in chordProgression:
        lyra.chord_to_guitar(chord)

    return

if __name__ == '__main__':
    main()
