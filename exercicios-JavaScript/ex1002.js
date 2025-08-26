let input = require('fs').readFileSync('/dev/stdin', 'utf8');
let lines = input.split('\n');
let r = parseFloat(lines.shift());
const pi = parseFloat('3.14159');
let a = pi*(r**2);
console.log(`A=${a.toFixed(4)}`)