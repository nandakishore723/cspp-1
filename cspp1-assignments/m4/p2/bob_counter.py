'''@author : nandakishore723
Assume s is a string of lower case characters.
Write a program that prints the number of times the string 'bob' occurs in s.
For example, if s = 'azcbobobegghakl', then your program should print
Number of times bob occurs is: 2'''

def main():
	string = input()
	#print(string)
	string_to_find = 'bob'
	count = 0
	for i in range(len(string)-2):
		if i in string_to_find:
			count = count + 1
		print(count)

    # string = input()
    # string_to_find = 'bob'
    # t_c = 0
    # for i in range(len(string)-2):
    #     b_c = 0
    #     n_r = 0
    #     o_r = i
    #     while (n_r < 3 and string[o_r] == string_to_find[n_r]):
    #         b_c = b_c + 1
    #         n_r = n_r + 1
    #         o_r = o_r + 1
    #     if b_c == 3:
    #         t_c = t_c + 1
    # print(t_c)
    
if __name__ == "__main__":
    main()
