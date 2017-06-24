def solution(arr, x, y):
	current_distance = None
	distances = []
	element = None

	if x == y: return 0
	if (not x in arr) or (not y in arr): return -1

	for i in range(0, len(arr)):
		if (arr[i] == x or arr[i] == y) and (element is None):
			element = arr[i]
			current_distance = 0
		elif (arr[i] == x or arr[i] == y) and (element is not None):
			if element != arr[i]:
				distances.append(current_distance)
				element = arr[i]
			# 	current_distance = 0
			# else:
			current_distance = 0
		elif (element is not None):
			current_distance += 1

	return (distances, min(distances))

print solution([6,3,3,7,7,7,7,7,5,6,3,2,3,5,6,6,2,34,7,3,5,6,7,3,6,2,3,7], 7,6)
print solution([1,2,1,1,1,1,1,1,5,1,2,1,2,2,2,3,3,3,3,2,2,2,2,1,1,1,1,5,1,1,1,1,1,2,5,5,2], 2,4)
print solution([2], 2,2)
