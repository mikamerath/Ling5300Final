import re
import sys
from time import sleep

from collections import Counter

player_name = ""
text_speed_name = "medium"
text_speed = 0.05

pass_phrases = ["In order to understand the world, we must first understand how information is transmitted and received", "We shouldn't be looking for heroes, we should be looking for good ideas"]
locations = ["Woods of Connection", "Finite State Automata Ruins", "Grammar Mountains"]
results = [False, False, False]

known_phrases = []

player_word_counts = Counter()

player_bigram_counts = Counter()

def set_text_speed(speed):
    global text_speed
    global text_speed_name
    text_speed_name = speed
    if re.match(r"[Ss]low", speed):
        text_speed = 0.1
    elif re.match(r"[Mm]edium", speed):
        text_speed = 0.05
    elif re.match(r"[Ff]ast", speed):
        text_speed = 0.025
    else:
        slow_print("I don't understand, setting speed to medium")
        text_speed = 0.05
        text_speed_name = "medium"

def slow_print(text):
    global text_speed
    for letter in text:
        sys.stdout.write(letter)
        sys.stdout.flush()
        sleep(float(text_speed))
    sys.stdout.write("\n")
    sys.stdout.flush()


def tokenize(text):
    return re.findall(r"\w+", text)


def add_player_string_to_counts(text):
    tokenized = tokenize(text)

    for i in range(len(tokenized) - 1):
        player_bigram_counts[(tokenized[i].lower(), tokenized[i+1].lower())] += 1
        player_word_counts[tokenized[i+1]] += 1
    player_word_counts[tokenized[0]] += 1


def get_player_word_count():
    return player_word_counts.total()

def get_n_most_common_words(n):
    return player_word_counts.most_common(n)


def get_n_most_common_bigrams(n):
    return player_bigram_counts.most_common(n)


def get_word_frequency(word):
    return player_word_counts[word] / player_bigram_counts.total()


def get_bigram_frequency(word1, word2):
    return player_bigram_counts[(word1, word2)] / player_bigram_counts.total()

def get_player_response(text=""):
    slow_print(text)
    response = input("\n" + player_name + ": ")
    add_player_string_to_counts(response)

    return response