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
    k = cu_a//2
    flag = 0
    for i in range(k):
        if i**3 == cu_a:
            flag = 1
    if flag == 1:
        print(cu_a, 'is a perfect cube')
    else:
        print(cu_a, 'is not a perfect cube')
if __name__ == "__main__":
    main()
