'''
@author : nandakishore723
Exercise: Assignment-1
The first step is to implement some code that
allows us to calculate the score for a single word.
The function get_word_score should accept as input a string
of lowercase letters (a word) and return the integer
score for that word, using the game's scoring rules.
'''
SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1,
    'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1,
    's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}
def get_word_score(word, n_num):
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
    sum = 0
    for i in word:
        sum = sum + SCRABBLE_LETTER_VALUES[i]
    sum = sum*len(word)
    if n_num == len(word):
        return sum + 50
    return sum
    '''
    sum_a = 0
    for i_a in word:
        if i_a in SCRABBLE_LETTER_VALUES:
            sum_a += SCRABBLE_LETTER_VALUES[i]
    sum_a = sum_a * len(word)
    if len(word) == n_num:
        sum_a = sum_a + 50
    return sum_a*len(word)
    '''
def main():
    '''
    Main function for the given problem
    '''
    word = input()
    word = word.split()
    print(get_word_score(word[0], int(word[1])))
if __name__ == "__main__":
    main()
