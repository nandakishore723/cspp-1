'''@author : nandakishore723
Assume s is a string of lower case characters.
Write a program that prints the number of times the string 'bob' occurs in s.
For example, if s = 'azcbobobegghakl', then your program should print
Number of times bob occurs is: 2'''

def main():
    '''Write a program that prints the number of times the string 'bob' occurs
    in s.'''
    s_a = input()
    s_b = 'bob'
    t_c = 0
    for m_r in range(len(s_a)):
        b_c = 0
        n_r = 0
        o_r = m_r
        while (n_r < 3 and s_a[o_r] == s_b[n_r]):
            b_c = b_c + 1
            n_r = n_r + 1
            o_r = o_r + 1
        if b_c == 3:
            t_c = t_c + 1
    print(t_c)
if __name__ == "__main__":
    main()
