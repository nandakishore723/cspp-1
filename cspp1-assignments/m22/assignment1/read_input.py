'''
@author : nandakishore723
Write a python program to read multiple lines of text input and
store the input into a string.
'''
def main():
	#reading lines
    lines = int(input())
    s_l = []
    for i in range(lines):
        s_l.append(input())
    for i in s_l:
        print(i)
if __name__ == '__main__':
    main()
