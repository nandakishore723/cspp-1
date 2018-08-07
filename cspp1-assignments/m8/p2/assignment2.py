'''
@author : nandakishore723
# Exercise: Assignment-2
# Write a Python function, sumofdigits, that takes in one number
# and returns the sum of digits of given number.
# This function takes in one number and returns one number.
'''
def sumofdigits(n_a):
    '''
    finding the sum of the digits
    '''
    if n_a == 0:
        return 0
    return (n_a%10) + sumofdigits(n_a//10)
def main():
    '''
    finding the sum of the digits
    '''
    a_a = int(input())
    print(sumofdigits(int(a_a)))
if __name__ == "__main__":
    main()
