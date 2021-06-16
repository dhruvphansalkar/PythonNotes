# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
from numpy import numpy as np

print("Hello world")

A = np.array([
    [5, 6, 6, 8],
    [2, 2, 2, 8],
    [6, 6, 2, 8],
    [2, 3, 6, 7]
], dtype=np.float_)

print("\n")


def fixRowZero(A):
    if A[0, 0] == 0:
        A[0] = A[0] + A[1]
    if A[0, 0] == 0:
        A[0] = A[0] + A[2]
    if A[0, 0] == 0:
        A[0] = A[0] + A[3]
    if A[0, 0] == 0:
        raise Exception("Matrix cannot be converted to echelon format. Matrix is singular")
    A[0] = A[0] / A[0, 0]
    print(A)
    return A


def fixRowOne(A):
    A[1] = A[1] - A[1, 0] * A[0]
    if A[1, 1] == 0:
        A[1] = A[1] + A[2]
        A[1] = A[1] - A[1, 0] * A[0]
    if A[1, 1] == 0:
        A[1] = A[1] + A[3]
        A[1] = A[1] - A[1, 0] * A[0]
    if A[1, 1] == 0:
        raise Exception("Matrix cannot be converted to echelon format. Matrix is singular")
    A[1] = A[1] / A[1, 1]
    print(A)
    return A


def fixRowTwo(A):
    A[2] = A[2] - A[2, 0] * A[0]
    A[2] = A[2] - A[2, 1] * A[1]
    if A[2, 2] == 0:
        A[2] = A[2] + A[3];
        A[2] = A[2] - A[2, 0] * A[0]
        A[2] = A[2] - A[2, 1] * A[1]
    if A[2, 2] == 0:
        raise Exception("Matrix cannot be converted to echelon format. Matrix is singular")
    A[2] = A[2] / A[2, 2]
    print(A)
    return A


def fixRowThree(A):
    A[3] = A[3] - A[3, 0] * A[0]
    A[3] = A[3] - A[3, 1] * A[1]
    A[3] = A[3] - A[3, 2] * A[2]
    if A[3, 3] == 0:
        raise MatrixIsSingular()
    A[3] = A[3] / A[3, 3]
    print(A)
    return A


A = fixRowZero(A)
A = fixRowOne(A)
A = fixRowTwo(A)
A = fixRowThree(A)