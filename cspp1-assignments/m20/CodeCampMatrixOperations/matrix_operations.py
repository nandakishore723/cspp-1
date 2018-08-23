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

def add_matrix(m1, m2):
    '''
        check if the matrix shapes are similar
        add the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for addition
        and return None
        error message should be "Error: Matrix shapes invalid for addition"
    '''
    Z = []
    for i in range(0,len(m1)):
        for column in range(0, len(m1[i])):
            result = m1[i][column] + m2[i][column]
            Z[i][j] = (result)
    return Z

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
            print("error: invalid input")
            return None
    return mat

def main():
    # read matrix 1
    matrix1 = read_matrix()
    # read matrix 2
    matrix2 = read_matrix()
    # add matrix 1 and matrix 2
    print(add_matrix(matrix1,matrix2))
    # multiply matrix 1 and matrix 2
    print(mult_matrix(matrix1,maatrix2))
if __name__ == '__main__':
    main()
