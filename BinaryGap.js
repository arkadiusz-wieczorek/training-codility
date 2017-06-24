function solution(N) {
	let bin = (N >>> 0).toString(2).split("");
	let longest = 0;

	while (bin[0] == 0) bin.shift();
	bin.reverse();

	while (bin[0] == 0) bin.shift();
	bin = bin.join("").split("1");

	for (let i = 0; i < bin.length - 1; i++) {
		if (longest < bin[i].length) longest = bin[i].length;
	}
	return longest;
}
