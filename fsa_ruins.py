import re

import helpers
from helpers import slow_print, get_player_response

# Stephen Kleene and Ken Thompson

puzzles = [r"[Ww]hy[\w\s]+\?$", r"[Ww]hat[\w\s]+ you are doing here\?$", r"^[Tt]he[\w\s]+\bis [0-9]+$", r"[\w\s]+ \$(?:[0-9]{3},)+[0-9]{3}\.[0-9]{2}$", r"^[Ii]{3}[\w\s]+[qvr].*[xyz][\w\s]+\w*m$"]
PASS_PHRASE_NUM = 1

def begin():
    if helpers.results[1]:
        slow_print("You return to the ruins, and reexamine the slab, happy with your progress knowing that you solved the five puzzles." +
                   "\nThere isn't much left to do here, and you feel a pull to return back to Santosan")
        return True
    
    slow_print("You trek across the stony path leading east. While traveling, you embarassingly trip over a rock and stumble down a small hill." + 
               "\nAs you stand up and gather yourself, you notice that you are in the middle of the fabled Finite State Automata Ruins")
    response = get_player_response("What would you like to do?")
    if re.match(r"[\w\s]*(?:[Ii]nvestigate|[Ll]ook around|[Ss]earch|[Dd]elve|[Ee]xamine|[Ee]xplore|[Ii]nspect)[\w\s]*", response):
        result = puzzle()
        return result
    elif re.match(r"[\w\s]*(?:[Ll]eave|[Rr]eturn|[Ss]antosan|[Gg]ive up)[\w\s]*"):
        slow_print("Unsure of what to do, you head back to the village of Santosan")
        return False

def puzzle():
    slow_print("After searching the area for a some time, You come to a slab of stone with strange symbols carved on it" +
               "\nOn it, you see some strange symbols:\n" +
               "\n".join(puzzles) +
               "\nA console slides out and prompts you to start typing\n\n")
    
    for i in range(len(puzzles)):
        response = ""
        while True:
            response = get_player_response("Console: " + puzzles[i])
            if re.match(puzzles[i], response):
                slow_print("Console: Correct! Well done!")
                break
            elif re.match(r"[\w\s]*([Gg]ive up|[Ll]eave|[Ss]mash|[Qq]uit)[\w\s]*", response):
                response = response.replace("I ", "")
                slow_print("Frustrated, you " + response + " and decide to return to Santosan")
                return False
            else:
                slow_print("That is an incorrect response" +
                           "\nThe console prints out: " + puzzles[i])
                
    slow_print("As you enter your final response, the console flashes a message across the screen:" +
               "\n\n" + "\"" + helpers.pass_phrases[PASS_PHRASE_NUM] + "\"")
    helpers.add_pass_phrase_to_player(PASS_PHRASE_NUM)

    return True