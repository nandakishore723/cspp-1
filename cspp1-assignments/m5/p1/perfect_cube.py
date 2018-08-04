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
    '''
    finding perfect cube or not
    '''
    cu_a = int(input())
    gu_a = 1
    while (gu_a**3) < cu_a:
        gu_a = gu_a + 1
        if int(gu_a**3) == cu_a:
            print(cu_a, 'is perfect cube')
        else:
            print(cu_a, 'is not perfect cube')
if __name__ == "__main__":
    main()
