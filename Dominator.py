from collections import Counter

def solution(A):
    if len(A) == 0: return -1
    if len(A) == 1: return 0

    if len(A) > 1:
        arr = sorted(Counter(A).items(), key=lambda x: x[1], reverse=True)
        try:
            if arr[0][1] == arr[1][1]:
                return -1
            elif float(arr[0][1]) / float(len(A)) > 0.5:
                return A.index(arr[0][0])
            else:
                return -1
        except:
            return 0

    pass
