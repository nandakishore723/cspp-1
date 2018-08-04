'''
@author : nandakishore723
Write a short program that prints each number from 1 to num on a new line.
For each multiple of 3, print "Fizz" instead of the number.
For each multiple of 5, print "Buzz" instead of the number.
For numbers which are multiples of both 3 and 5, print "FizzBuzz" instead
of the number.
'''
def main():
    '''
    Read number from the input, store it in variable num.
    '''
    num = int(input())
    i = 0
    while i <= num-1:
    	i = i+1
    	if i%3 == 0:
    		print('Fizz')
    	elif i%5 == 0:
    		print('Buzz')
    	elif i%15 == 0:
    		print('FizzBuzz')
    	else:
    		print(i)
if __name__ == "__main__":
	main()
