

# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

def solution(A):
    
    temp_L = sum(A[:1])
    temp_R = sum(A[1:])
    difference = abs(temp_L - temp_R)
    
    for i in xrange (2, len(A)-1):
        L = sum(A[:i])
        R = sum(A[i:])
        temp_diff = abs(L-R)
        
        if temp_diff < difference:
            difference = temp_diff
            
        if difference == 0:
            break
    
    return difference
    pass


