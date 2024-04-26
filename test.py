import helpers

helpers.add_player_string_to_counts("This is the player counts, does it work? I'm adding the word again and this is the word")

print(helpers.get_n_most_common_words(3))
print("The word frequency of the: " + str(helpers.get_word_frequency("the")))
print("The most common bigrams are: " + str(helpers.get_n_most_common_bigrams(3)))
print("Getting bigram frequency of the word: " + str(helpers.get_bigram_frequency("the", "word")))