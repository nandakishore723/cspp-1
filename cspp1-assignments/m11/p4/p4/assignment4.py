'''
@author : nandakishore723
#Exercise: Assignment-4
#We are now ready to begin writing the code that interacts with the player.
# We'll be implementing the playHand function. This function allows the user
# to play out a single hand.
# First, though, you'll need to implement the helper calculateHandlen function,
#which can be done in under five lines of code.
'''
def calculate_handlen(hand):
    """
    Returns the length (number of letters) in the current hand.
    hand: dictionary (string int)
    returns: integer
    """
    sum_a = 0
    for iter_ in hand:
        sum_a += hand[iter_]
    return sum_a

def main():
    '''
    Returns the length (number of letters) in the current hand.
    hand: dictionary (string int)
    returns: integer
    '''
    n_num = input()
    adict = {}
    for data in range(int(n_num)):
        data = input()
        l_list = data.split()
        adict[l_list[0]] = int(l_list[1])
    print(calculate_handlen(adict))
if __name__ == "__main__":
    main()
