'''
@author : nandakishore723
# Exercise: Assignment-1
# Write a Python function, factorial(n), that takes in one
# number and returns the factorial of given number.
# This function takes in one number and returns one number.
'''
def factorial(n_a):
    '''
    finding the factorial of a number.
    '''
    if n_a == 0:
        return 1
    return n_a * factorial(n_a-1)
def main():
    '''
    finding the factorial of a number.
    '''
    a_a = input()
    print(factorial(int(a_a)))    
if __name__ == "__main__":
    main()
