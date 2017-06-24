function solution(arr, k) {
	let arr_length = arr.length;

	if (arr.length == 0) return arr;

	while (arr_length < k) {
		k = k - arr_length;
	}

	let temp_arr = [];
	for (i = 0; i < k; i++) {
		let element = arr.pop();
		temp_arr.push(element);
	}

	temp_arr.reverse();
	return temp_arr.concat(arr);
}
