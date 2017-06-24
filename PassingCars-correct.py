

# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

def solution(A):
    # write your code in Python 2.7

    zeros = 0
    counter = 0

    for i in range(0, len(A)):
        if A[i] == 0:
            zeros += 1
        elif A[i] == 1:
            counter = counter + zeros
        if counter > 1000000000: return -1

    return counter
    pass
