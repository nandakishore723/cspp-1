'''
Write a python program to read multiple lines of text input and store the input into a string.
'''
def ss(s):
    lines = ""
    for i in s:
        lines += input()+"\n"
def main():
    s = input()
    ss(s)
if __name__ == '__main__':
    main()
