'''
@author : nandakishore723
Given a  number int_input, find the product of all the digits
example: 
	input: 123
	output: 6
'''
def main():
    '''
    Read any number from the input, store it in variable int_input.
    '''
    int_input = int(input())
    i = 1
    p_a = 1
    for i in range(1,int_input + 1):
    	p_a = p_a*1
    	print(p_a*i)
    	i = i+1
if __name__ == "__main__":
    main()
