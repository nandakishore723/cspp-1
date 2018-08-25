'''
@author : nandakishore723
Write a python program to read multiple lines of text input and
store the input into a string.
'''
def main():
    lines = int(input())
    s = []
    for i in range(lines):
        s.append(input())
    for i in s:
        print(i)
if __name__ == '__main__':
    main()
