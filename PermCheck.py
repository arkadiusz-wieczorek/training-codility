def solution(arr):
    correct_perm = sorted(range(len(arr)+1)[1:])
    arr = sorted(arr)
    
    if correct_perm == arr: return 1
    else: return 0
    pass
