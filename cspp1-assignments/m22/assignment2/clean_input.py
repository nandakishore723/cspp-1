'''
@author : nandakishore723
Write a function to clean up a given string by removing the special
characters and retain alphabets in both upper and lower case and numbers.
'''
import re
#import math
def cleaning_string(string):
    """clean"""
    return re.sub('[^a-zA-Z0-9]', '', string)

def main():
    """main"""
    string = input()
    print(cleaning_string(string))

if __name__ == '__main__':
    main()
