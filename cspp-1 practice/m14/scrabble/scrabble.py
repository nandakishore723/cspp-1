'''
@author: nandakishore723
# The 6.00 Word Game
'''
import random
# import string

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1,
    'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1,
    's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}
WORD_LIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # in_file: file
    in_file = open(WORD_LIST_FILENAME, 'r')
    # word_list: list of strings
    word_list = []
    for line in in_file:
        word_list.append(line.strip().lower())
    print(" ", len(word_list), "words loaded.")
    return word_list

def get_freuency_dict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """
    # freqs: dictionary (element_type -> int)
    freq = {}
    for x_in in sequence:
        freq[x_in] = freq.get(x_in, 0) + 1
    return freq

# Problem #1: Scoring a word

def get_wordscore(word, n_in):
    """
    Returns the score for a word. Assumes the word is a valid word.

    The score for a word is the sum of the points for letters in the
    word, multiplied by the length of the word, PLUS 50 points if all n
    letters are used on the first turn.

    Letters are scored as in Scrabble; A is worth 1, B is worth 3, C is
    worth 3, D is worth 2, E is worth 1, and so on (see SCRABBLE_LETTER_VALUES)

    word: string (lowercase letters)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    returns: int >= 0
    """
    count = 0
    for i in word:
        if i in SCRABBLE_LETTER_VALUES:
            count = count + SCRABBLE_LETTER_VALUES[i]
        if len(word) == n_in:
            return (count * len(word) + 50)
        return (count * len(word))

# Problem #2: Make sure you understand how this function works and what it does!

def display_hand(hand):
    """
    Displays the letters currently in the hand.

    For example:
    >>>display_hand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
    >>>a x x l l l e
    The order of the letters is unimportant.

    hand: dictionary (string -> int)
    """
    for letter in hand.keys():
        for j in range(hand[letter]):
            print(letter, end="")              # print all on the same line
    print()                               # print an empty line
#
# Problem #2: Make sure you understand how this function works and what it does!
#
def deal_hand(n_in):
    """
    Returns a random hand containing n lowercase letters.
    At least n/3 the letters in the hand should be VOWELS.

    Hands are represented as dictionaries. The keys are
    letters and the values are the number of times the
    particular letter is repeated in that hand.

    n: int >= 0
    returns: dictionary (string -> int)
    """
    hand = {}
    num_vowels = n_in // 3

    for i in range(num_vowels):
        x_in = VOWELS[random.randrange(0, len(VOWELS))]
        hand[x_in] = hand.get(x_in, 0) + 1

    for i in range(num_vowels, n_in):
        x_in = CONSONANTS[random.randrange(0, len(CONSONANTS))]
        hand[x_in] = hand.get(x_in, 0) + 1

    return hand

# Problem #2: Update a hand by removing letters

def update_hand(hand, word):
    """
    Assumes that 'hand' has all the letters in word.
    In other words, this assumes that however many times
    a letter appears in 'word', 'hand' has at least as
    many of that letter in it.

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.
    word: string
    hand: dictionary (string -> int)
    returns: dictionary (string -> int)
    """
    update_hand = hand.copy()
    for i in word:
        if i in update_hand:
            update_hand[i] -= 1
    return update_hand

# Problem #3: Test word validity

def is_valid_word(word, hand, word_list):
    """
    Returns True if word is in the word_list and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or word_list.

    word: string
    hand: dictionary (string -> int)
    word_list: list of lowercase strings
    """
    hand_xerox = dict(hand)
    letter_count = 0
    if word in word_list:
        for letter in word:
            if letter in hand_xerox and hand[letter] > 0:
                hand_xerox[letter] -= 1
                letter_count += 1
    return bool(letter_count == len(word))

# Problem #4: Playing a hand

def calculate_hand_length(hand):
    """
    Returns the length (number of letters) in the current hand.

    hand: dictionary (string-> int)
    returns: integer
    """
    return sum(hand.values())

def play_hand(hand, word_list, n_in):
    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.
    * The user may input a word or a single period (the string ".")
      to indicate they're done playing
    * Invalid words are rejected, and a message is displayed asking
      the user to choose another word until they enter a valid word or "."
    * When a valid word is entered, it uses up letters from the hand.
    * After every valid word: the score for that word is displayed,
      the remaining letters in the hand are displayed, and the user
      is asked to input another word.
    * The sum of the word scores is displayed when the hand finishes.
    * The hand finishes when there are no more unused letters or the user
      inputs a "."

      hand: dictionary (string -> int)
      word_list: list of lowercase strings
      n: integer (HAND_SIZE; i.e., hand size required for additional points)

    """
    # BEGIN PSEUDOCODE <-- Remove this comment when you code this function;
    # do your coding within the pseudocode (leaving those comments in-place!)
    # Keep track of the total score

    # As long as there are still letters left in the hand:
    total_score = 0
    while calculate_hand_length(hand) > 0:
        # Display the hand
        display_hand(hand)
        # Ask user for input
        user_input = input()
        # If the input is a single period:
        if user_input == '.' or user_input == 'e':
            print("Game over")
            # End the game (break out of the loop)
            break
        # Otherwise (the input is not a single period):
        else:
            # If the word is not valid:
            if not is_valid_word(user_input, hand, word_list):
                # Reject invalid word (print a message followed by a blank line)
                print("Invalid word")
            # Otherwise (the word is valid):
            else:
                # Tell the user how many points the word earned, and the updated
                # total score, in one line followed by a blank line
                word_score = get_wordscore(user_input, n_in)
                total_score += word_score
                print("You've earned {}, your score now is {}".format(word_score, total_score))
                # Update the hand
                hand = update_hand(hand, user_input)
    # Game is over (user entered a '.' or ran out of letters), so tell user the
    # total score
    print("Total Score = {}".format(total_score))

# Problem #5: Playing a game

def play_game(word_list):
    """
    Allow the user to play an arbitrary number of hands.

    1) Asks the user to input 'n' or 'r' or 'e'.
      * If the user inputs 'n', let the user play a new (random) hand.
      * If the user inputs 'r', let the user play the last hand again.
      * If the user inputs 'e', exit the game.
      * If the user inputs anything else, tell them their input was invalid.

    2) When done playing the hand, repeat from step 1
    """
    # TO DO ... <-- Remove this comment when you code this function
    hand = {}
    while True:
        user_input = input("Enter a input n(for new hand) or r(to play last hand)\
        or e(exit the game)")
        if user_input == 'n':
            hand = deal_hand(HAND_SIZE)
            play_hand(hand, word_list, HAND_SIZE)
        elif user_input == 'r':
            play_hand(hand, word_list, HAND_SIZE)
        elif user_input == 'e':
            print("Game Over!")
            break
        else:
            print("Invalid input")

# Build data structures used for entire session and play game

if __name__ == '__main__':
    WORD_LIST = load_words()
    play_game(WORD_LIST)
