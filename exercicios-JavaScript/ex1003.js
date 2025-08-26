let input = require('fs').readFileSync('/dev/stdin', 'utf8');
let lines = input.split('\n');
a = parseInt(lines.shift());
b = parseInt(lines.shift());
console.log(`SOMA = ${a + b}`)