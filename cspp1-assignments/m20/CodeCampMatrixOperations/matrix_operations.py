'''
@author : nandakishore723
'''
def mult_matrix(m1, m2):
    '''
        check if the matrix1 columns = matrix2 rows
        mult the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for mult
        and return None
        error message should be "Error: Matrix shapes invalid for mult"
    '''
    '''rows, columns = len(matrix1), len(matrix2[0])
    matrix = [[0] * columns for _ in range(rows)]
    for i in range(rows):
        for j in range(columns):
            result[i][j] = sum(matrix1[i][k] * matrix2[k][j]
                for k in range(len(matrix2))):
    return result
    '''
    add_m = re_mat(len(m1), len(m1[0]))
    if len(m1[0]) == len(m2):
        for i in range(len(m1)):
            for j in range(len(m2[0])):
                for k in range(len(m2)):
                    add_m[i][j] += m1[i][j] * m2[k][j]
        return add_m
    else:
        print("Error : Matrix shapes invalid for mult")
        return None
        
def re_mat(rows, columns):
    add_matrix = [[0 for i in range(columns)] for i in range(rows)]
    return (add_matrix)

def add_matrix(m1, m2):
    '''
        check if the matrix shapes are similar
        add the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for addition
        and return None
        error message should be "Error: Matrix shapes invalid for addition"
    '''
    add_m = re_matrix(len(m1), len(m1[0]))
    if len(m1[0]) == len(m2):
        for i in range(len(m1)):
            for j in range(len(m2[0])):
                for k in range(len(m2)):
                    add_m[i][j] += m1[i][k] * m2[k][j]
        return add_m
    else:
        print("Error: Matrix shapes invalid for mult")
        return None

def read_matrix():
    '''
        read the matrix dimensions from input
        create a list of lists and read the numbers into it
        in case there are not enough numbers given in the input
        print an error message and return None
        error message should be "Error: Invalid input for the matrix"
    '''
    mat = []
    list_input = input().split(",")
    rows, columns = int(list_input[0]), int(list_input[1])
    for _ in range(rows):
        list_mat_row = input().split()
        if columns == len(list_mat_row):
            mat.append([int(i) for i in list_mat_row])
        else:
            print("Error: Ivalid input for the matrix")
            return None
    return mat

def main():
    # read matrix 1
    matrix1 = read_matrix()
    if m1 is None:
        exit()
    # read matrix 2
    matrix2 = read_matrix()
    if m2 is None:
        exit()
    # add matrix 1 and matrix 2
    print(add_matrix(matrix1, matrix2))
    # multiply matrix 1 and matrix 2
    print(mult_matrix(matrix1, matrix2))
if __name__ == '__main__':
    main()
