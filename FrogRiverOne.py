def solution(position, arr):    
    required_leaves = set(range(position+1)[1:])
    
    for i in xrange(0,len(arr)):
        if arr[i] in required_leaves:
            required_leaves.remove(arr[i])
            if len(required_leaves) == 0: return i
            
    if len(required_leaves) != 0: return -1
    pass
