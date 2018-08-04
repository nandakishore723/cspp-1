'''
@author : nandakishore723
Write a python program to find if the given number is a perfect cube or not
using guess and check algorithm

testcase 1
Input: 24389
Output: 24389 is a perfect cube

testcase 2
Input: 21950
Output: 21950 is not a perfect cube
'''

def main():
	ep = 0.01
	step = 0.1
	sq = int(input())
	gu = 0.0
	while gu <= sq:
		if abs(gu**2-sq) < ep:
			break
	else:
		gu = gu + step
print(str(gu))
if __name__== "__main__":
	main()
