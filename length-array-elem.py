def solution(arr, x, y):
	first = None
	curr_distance = None
	# min_distance = None
	distances = []

	for i in range(0, len(arr)):
		if (arr[i] == x or arr[i] == y) and (first is None):
			first = arr[i]
			curr_distance = 0
		elif arr[i] == x or arr[i] == y:
			if first != arr[i]:
				distances.append(curr_distance)
				first = arr[i]
			curr_distance = 0
		elif first is not None:
			curr_distance += 1


	pass
	print distances, min(distances)

solution([1,2,1,1,1,1,1,1,5,1,2,1,2,2,2,3,3,3,3,2,2,2,2,1,1,1,1,5,1,1,1,1,1,2,5,5,2], 2,5)
