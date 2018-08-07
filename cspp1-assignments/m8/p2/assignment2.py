'''
@author : nandakishore723
# Exercise: Assignment-2
# Write a Python function, sumofdigits, that takes in one number
# and returns the sum of digits of given number.
# This function takes in one number and returns one number.
'''
def sumofdigits(n):
    '''
    finding the sum of the digits
    '''
    if n == 0:
        return 0
    else:
        return (n%10) + sumofdigits(n//10)
def main():
    '''
    finding the sum of the digits
    '''
    a = int(input())
    print(sumofdigits(int(a)))
if __name__ == "__main__":
    main()
