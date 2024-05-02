
import helpers
from helpers import slow_print

FIRST_TIME = True

def begin():
    global FIRST_TIME
    if FIRST_TIME and not helpers.get_finished():
        slow_print("\"Greetings, young one!\" the old woman proclaims as you step into her home." +
                   "\nI have a very special surprise for you. But first, you must explore the" +
                   "\nsurrounding areas and return to me when you have discovered their secrets." +
                   "\nA little disappointed, you return to Santosan.")
        FIRST_TIME = False
        return
    
    slow_print("You enter the old woman's house and she turns around on your arrival.")
    if not helpers.get_finished():
        slow_print("I'm sorry, but you have not solved all of the puzzles in the area, I cannot give you a reward.")
        return
    
    slow_print("\"You have completed all challenges! Congratulations, you truly are a big deal\" the woman says." +
               "\nShe smiles at you and hands you a locket. \"It will grant you one wish\" the woman continues." +
               "\n\"But that's a story for another time. As you exit her house, you feel exhausted by your accomplishments" +
               "\nfor the day. You head back home and quickly fall asleep.")
    return True