import fs = require('fs');

const input = process.platform === 'linux' ?
	fs.readFileSync('/dev/stdin').toString() :
	'4'
		.split(' ')

const N = parseInt(input[0])
for (let i = 1; i <= 9; i++) {
	console.log(N, "*", i, "=", N * i)
}