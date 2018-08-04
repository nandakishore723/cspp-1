'''
@author : nandakishore723
Write a python program to find the square root of the given number
using approximation method
testcase 1
input: 25
output: 4.999999999999998
testcase 2
input: 49
output: 6.999999999999991
'''
def main():
    '''
    finding square root of the number
    '''
    epsilon = 0.01
    step = 0.1
    square = 0.1
    guess = 0.0
    while guess <= square:
        if abs(guess**2-square) < epsilon:
            break
        else:
            guess = guess + step
    print(str(guess))
if __name__ == "__main__":
    main()
