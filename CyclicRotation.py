def solution(arr, k):

    if (arr == [] or k == 0): return arr

    while(k > len(arr)):
        k = k - len(arr)
        pass

    if (k == len(arr)): return arr

    return arr[len(arr)-k:] + arr[0:len(arr)-k]


    pass
