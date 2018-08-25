'''
@author : nandakishore723
Write a function to clean up a given string by removing the special
characters and retain alphabets in both upper and lower case and numbers.
'''
import re
#import math
def clean_string(str_a):

    return re.sub('[^a-zA-Z0-9]', '', str_a)

def main():
	'''This is main function'''
    string = input()
    print(clean_string(str_a))
if __name__ == '__main__':
    main()
