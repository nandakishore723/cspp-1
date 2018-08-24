'''
@author : nandakishore723
Below are the possible values that a valid game grid could contain:
x - A character representing Player-1’s move
o - A character representing Player-2’s move
. - Empty
Based on the game input, there can be following outputs:
x or o? - winning player from the grid
draw? - when the game is a draw
invalid input? - when the game input doesn’t have valid characters
invalid game? - where the game data has valid characters but the game
rules are not followed
'''
def count_mat(mat, cnt_var):
    '''
    counting the values
    '''
    count1 = 0
    for word in mat:
        count1 += word.count(cnt_var)
    return count1

def is_validation(mat):
    '''
    validation of matrices
    '''
    for i in mat:
        for j in i:
            if j not  in 'xo.':
                print("invalid input")
                return False
    if (count_mat(mat, 'x') == 4 and count_mat(mat, 'o') == 5)  or \
     (count_mat(mat, 'x') == 5 and count_mat(mat, 'o') == 4):
        print("draw")
        return False
    if (count_mat(mat, 'x') > 5) or (count_mat(mat, 'o') > 5) or\
     count_mat(mat, 'x') == count_mat(mat, 'o'):
        print("invalid game")
        return False
    return True

def result_int(mat):
    '''
    result of input
    '''
    if mat[0][0] == mat[1][1] == mat[2][2]:
        return mat[0][0]
    elif mat[0][0] == mat[0][1] == mat[0][2]:
        return mat[0][1]
    elif mat[1][0] == mat[1][1] == mat[1][2]:
        return mat[1][0]
    elif mat[2][0] == mat[2][1] == mat[2][2]:
        return mat[2][0]
    elif mat[0][0] == mat[1][0] == mat[2][0]:
        return mat[0][0]
    elif mat[0][1] == mat[1][1] == mat[2][1]:
        return mat[0][1]
    elif mat[0][2] == mat[1][2] == mat[2][2]:
        return mat[0][2]
    elif mat[2][0] == mat[1][1] == mat[0][2]:
        return mat[2][0]
    print("invalid input")

def read_input():
    '''
    read the input
    '''
    matrix = []
    for _ in range(3):
        list_input = input().split(" ")
        matrix.append(list_input)
    return matrix

def main():
    '''
    main function
    '''
    mat = read_input()
    if is_validation(mat):
        print(result_int(mat))
main()
