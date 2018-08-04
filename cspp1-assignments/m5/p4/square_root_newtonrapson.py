'''
@author : nandakishore723
Write a python program to find the square root of the given number
using approximation method
testcase 1
input: 25
output: 4.999999999999998
testcase 2
input: 49
output: 6.999999999999991
'''
def main():
    '''
    finding the square root of the given number
    '''
    epsilon = 0.01
    x_num = int(input())
    gu_val = x_num/2.0
    while abs(gu_val*gu_val - x_num) >= epsilon:
        gu_val = gu_val - (((gu_val**2) - x_num)/(2*gu_val))
        print(str(gu_val))
if __name__ == "__main__":
    main()
