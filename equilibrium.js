function sum(arr) {
	return arr.reduce((acc, val) => acc + val, 0);
}

function solution(arr) {
	if (sum(arr) === arr[0]) return 0;

	let start = 1;

	while (start < arr.length) {
		let L = arr.slice(0, start);
		let R = arr.slice(start + 1);

		if (sum(L) == sum(R)) return start;
		start++;
	}

	return -1;
}
// https://codility.com/demo/results/demoFDS5BG-TBQ/
