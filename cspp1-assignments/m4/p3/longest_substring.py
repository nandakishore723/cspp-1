'''
@author = nandakishore723
Assume s is a string of lower case characters.

Write a program that prints the longest substring of s in which the
letters occur in alphabetical order.
For example, if s = 'azcbobobegghakl', then your program should print

Longest substring in alphabetical order is: beggh

In the case of ties, print the first substring.
For example, if s = 'abcbcd', then your program should print

Longest substring in alphabetical order is: abc

Note: This problem may be challenging. We encourage you to work smart.
If you've spent more than a few hours on this problem, we suggest that
you move on to a different part of the course.
If you have time, come back to this problem after you've had a break and
cleared your head.
 '''
def main():
    '''Assume s is a string of lower case characters.
Write a program that prints the longest substring of s in which the
letters occur in alphabetical order.
    '''
    s_a = input()
    temp_s = ""
    for m_r in range(len(s_a)-1):
        s_s = s_a[m_r]
        while m_r+1 < len(s_a) and s_a[m_r] <= s_a[m_r+1]:
            m_r = m_r + 1
            s_s = s_s + s_a[m_r]
        if len(s_s) > len(temp_s):
            temp_s = s_s
    print(temp_s)
if __name__ == "__main__":
    main()
