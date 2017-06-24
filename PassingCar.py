def solution(arr):
    pairs = set()

    for i in range(0, len(arr)):
        if arr[i] == 0:
            P = i
            for j in range(i+1, len(arr)):
                if arr[j] == 1:
                    pairs.add((P,j))

	if len(pairs) > 1000000000: return -1
	else: len(pairs)


# a = [0, 1, 0, 1, 1]
# solution(a)
# # 0 -> 1

# 0 <= P < Q < N
# P --->
# Q <---
