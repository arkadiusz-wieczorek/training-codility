function solution(A) {
	let arr = A.sort((a, b) => a - b);

	for (let i = 0; i < arr.length - 1; i++) {
		if (arr[i] == arr[i + 1]) {
			// arr.splice(i, 2);
			// i = 0;
			(arr[i] = undefined), (arr[i + 1] = undefined);
		}
	}

	arr = arr.filter(function(n) {
		return n != undefined;
	});
	if (arr.length == 1) return arr[0];
	if (arr[arr.length - 2] !== arr[arr.length - 1]) return arr[arr.length - 1];
	else return arr[0];
}
