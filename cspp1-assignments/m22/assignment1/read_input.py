'''
@author : nandakishore723
Write a python program to read multiple lines of text input and
store the input into a string.
'''
def main():
	'''
	reading multiple lines
	'''
    lines = int(input())
    st_lis = []
    for i in range(lines):
        st_lis.append(input())
    for i in st_lis:
        print(i)
if __name__ == '__main__':
    main()
