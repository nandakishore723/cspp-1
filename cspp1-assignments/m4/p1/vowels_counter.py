'''
@author : nandakishore723
Assume s is a string of lower case characters.
Write a program that counts up the number of vowels contained in the string s.
Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. For example, if s = 'azcbobobegghakl',
your program should print:
Number of vowels: 5
'''
def main():
    '''
Assume s is a string of lower case characters.
Write a program that counts up the number of vowels contained in
the string s.
    '''
    s_a = input()
    s_b = 0
    for var_v in s_a:
        if var_v in 'aeiou':
            s_b = s_b + 1
    print(s_b)
if __name__ == "__main__":
    main()
