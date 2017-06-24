def solution(a, b, k):

	counter = 0

	start_chunk = a
	end_chunk = b
	size_chunk = 1


	while(end_chunk > start_chunk and size_chunk <100):
		size_chunk = size_chunk*10

	while (end_chunk >= start_chunk):
		arr_range = range(start_chunk, start_chunk+size_chunk+1)

		values = filter(lambda el: el % k == 0, arr_range)
		counter += len(values)
		print arr_range
		start_chunk = start_chunk+size_chunk+1
		pass

	print counter



	# naiwne------------------
	# arr_range = range(a,b+1)
	# values = filter(lambda el: el % k == 0, arr_range)
	#
	# print len(values)
	# return len(values)

solution(6,11,2)

# solution(0,20000,41235)
