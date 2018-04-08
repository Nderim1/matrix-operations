import math
from math import sqrt
import numbers
from copy import deepcopy

def zeroes(height, width):
        """
        Creates a matrix of zeroes.
        """
        g = [[0.0 for _ in range(width)] for __ in range(height)]
        return Matrix(g)

def identity(n):
        """
        Creates a n x n identity matrix.
        """
        I = zeroes(n, n)
        for i in range(n):
            I.g[i][i] = 1.0
        return I

def minor(matrix,r=0,c=0): 
    minor = deepcopy(matrix)
    del minor[r]
    #delete row r
    for b in range(len(minor)):
        #Delete column c
        del minor[b][c]
    return minor

def recursive_det(matrix):
    if len(matrix) == 1:
          return matrix[0][0]
    else:
        # inspired by an answer in Stackoverflow
        determinant = 0
        for i in list(range(len(matrix))): #Iterates first row and find comatrixes
            determinant += matrix[0][i] * (-1)**(2+i) * recursive_det(minor(matrix,0,i))
        return determinant

def adjugate(matrix):
    minor_mx = minor_matrix(matrix)
    cofactor_mx = cofactor_matrix(minor_mx)
    transpose_mx = get_transpose(cofactor_mx)
    return transpose_mx

def minor_matrix(matrix):
    minor_matrix = []
    for i in range(len(matrix)):
        row = []
        for j in range(len(matrix)):
            minor_det = []
            minor_det = recursive_det(minor(matrix, i,j))
            row.append(minor_det)
        minor_matrix.append(row)
    return minor_matrix

def cofactor_matrix(matrix):
    cofactor_matrix = []
    for i in range(len(matrix)):
        row = []
        for j in range(len(matrix)):
            row.append(matrix[i][j]*(-1)**(2+i+j))
        cofactor_matrix.append(row)
    return cofactor_matrix

def get_transpose(matrix):
    matrix_transpose = []
    for i in range(len(matrix[0])):
        new_col = get_column(matrix, i)
        matrix_transpose.append(new_col)

    return matrix_transpose

def get_column(matrix, column_number):
    column = []
    for i in range(len(matrix)):
        column.append(matrix[i][column_number])
    
    return column

def is_mult_valid(first, other):
    is_valid = len(first[0]) == other.get_shape()[0]
    return is_valid

class Matrix(object):

    # Constructor
    def __init__(self, grid):
        self.g = grid
        self.h = len(grid)
        self.w = len(grid[0])

    #
    # Primary matrix math methods
    #############################
 
    def determinant(self):
        """
        Calculates the determinant of nxn matrix.
        """
        if not self.is_square():
            raise(ValueError, "Cannot calculate determinant of non-square matrix.")
        
        return recursive_det(self.g)

    def trace(self):
        """
        Calculates the trace of a matrix (sum of diagonal entries).
        """
        if not self.is_square():
            raise(ValueError, "Cannot calculate the trace of a non-square matrix.")

        # TODO - your code here
        trace = 0
        for i in range(self.h):
            trace += self.g[i][i]
        return trace

    def inverse(self):
        """
        Calculates the inverse of a 1x1 or 2x2 Matrix.
        """
        if not self.is_square():
            raise(ValueError, "Non-square Matrix does not have an inverse.")

        # TODO - your code here
        inverse = []
        adj = adjugate(self.g)
        identity = 1/recursive_det(self.g)
        for i in range(len(adj)):
            row = []
            for j in range(len(adj[i])):
                row.append(adj[i][j] * identity)
            inverse.append(row)
        return Matrix(inverse)

    def T(self):
        """
        Returns a transposed copy of this Matrix.
        """
        # TODO - your code here
        transpose = get_transpose(self.g)
        return Matrix(transpose)

    def is_square(self):
        return self.h == self.w

    def get_shape(self):
        return [self.h, self.w]
    #
    # Begin Operator Overloading
    ############################
    def __getitem__(self,idx):
        """
        Defines the behavior of using square brackets [] on instances
        of this class.

        Example:

        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > my_matrix[0]
          [1, 2]

        > my_matrix[0][0]
          1
        """
        return self.g[idx]

    def __repr__(self):
        """
        Defines the behavior of calling print on an instance of this class.
        """
        s = ""
        for row in self.g:
            s += " ".join(["{} ".format(x) for x in row])
            s += "\n"
        return s

    def __add__(self,other):
        """
        Defines the behavior of the + operator
        """
        if self.h != other.h or self.w != other.w:
            raise (ValueError, "Matrices can only be added if the dimensions are the same") 
        #   
        # TODO - your code here
        #
        sumM = []
        for i in range(self.h):
            row = []
            for j in range(self.w):
                row.append(self.g[i][j] + other[i][j])
            sumM.append(row)
        return Matrix(sumM)

    def __neg__(self):
        """
        Defines the behavior of - operator (NOT subtraction)

        Example:

        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > negative  = -my_matrix
        > print(negative)
          -1.0  -2.0
          -3.0  -4.0
        """
        #   
        # TODO - your code here
        #
        neg = []
        for i in range(self.h):
            row = []
            for j in range(self.w):
                row.append(self.g[i][j]*-1)
            neg.append(row)
        return Matrix(neg)

    def __sub__(self, other):
        """
        Defines the behavior of - operator (as subtraction)
        """
        #   
        # TODO - your code here
        #
        sub = []
        for i in range(self.h):
            row = []
            for j in range(self.w):
                row.append(self.g[i][j] - other[i][j])
            sub.append(row)
        return Matrix(sub)

    def __mul__(self, other):
        """
        Defines the behavior of * operator (matrix multiplication)
        """
        #   
        # TODO - your code here
        #
        if not is_mult_valid(self.g, other):
            raise(ValueError, "These matrices can not be multiplied: they should have dimensions nxm and mxn")

        mul = []
        for i in range(self.h):
            row = []
            for j in range(self.h):
                sumM = 0
                for r in range(other.h):
                    sumM += self.g[i][r] * other[r][j]
                row.append(sumM)
            mul.append(row)
        return Matrix(mul)

    def __rmul__(self, other):
        """
        Called when the thing on the left of the * is not a matrix.

        Example:

        > identity = Matrix([ [1,0], [0,1] ])
        > doubled  = 2 * identity
        > print(doubled)
          2.0  0.0
          0.0  2.0
        """
        if isinstance(other, numbers.Number):
            pass
            #   
            # TODO - your code here
            #
            result = []
            for i in range(self.h):
                row = []
                for j in range(self.w):
                    row.append(self[i][j]*other)
                result.append(row)
            return Matrix(result)
            