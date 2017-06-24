# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

def solution(arr):
    counter = 0

    zeros = [i for i, x in enumerate(arr) if x == 0]
    ones = [i for i, x in enumerate(arr) if x == 1]
    # for i in range(0, len(arr)):
    #     if arr[i] == 0: zeros.append(i)
        # else: ones.append(i)

    # for i in enumerate([2,3,5,6]):
    for i in range(0, len(zeros)):
        val = filter(lambda el: el > zeros[i], ones)
        ones = val
        counter += len(val)
        if counter > 1000000000: return -1

    return counter
    # print zeros, ones

    pass
