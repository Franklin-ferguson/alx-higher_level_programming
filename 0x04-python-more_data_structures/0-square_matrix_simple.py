#!/usr/bin/python3


def square_matrix_simple(matrix=[]):
    if not matrix:
        print()
    else:
        for row in range(len(matrix)):
            for item in range(len(matrix[row])):
                if item != len(matrix[row]) - 1:
                    endspace = " "
                else:
                    endspace = " "
                print("{:d}".format((matrix[row][item]) ** 2), end=endspace)
            print()
