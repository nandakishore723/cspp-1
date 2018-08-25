'''
@author : nandakishore723
Write a python program to read multiple lines of text input and
store the input into a string.
'''
def ss(s):
    lines = " "
    for i in s:
        if i not in lines:
            return False
        return True

def main():
    s = raw_input()
    ss(s)
if __name__ == '__main__':
    main()
