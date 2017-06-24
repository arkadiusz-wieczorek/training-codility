function solution(arr) {
	arr.sort((a, b) => a - b);
	if (arr.length == 0 || arr[0] != 1) return 1;

	for (let i = 0; i <= arr.length - 1; i++) {
		if (arr[i] + 1 != arr[i + 1]) return arr[i] + 1;
	}
}
