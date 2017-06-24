def solution(a, b, k):

    counter = 0

    for i in range(a,b+1):
        if i % k == 0:
            counter += 1

    return counter
