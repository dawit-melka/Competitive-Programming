"use strict";
process.stdin.resume();
process.stdin.setEncoding("utf-8");
 
let inputString = '';
let currentLine = 0;
 
process.stdin.on("data", (inputStdin) => {
  inputString += inputStdin;
});
process.stdin.on("end", () => {
  inputString = inputString.split(" ");
  main();
});
function readline() {
  return inputString[currentLine++];
}
 
// ********** Code Start **********

function main() {
var m = parseInt(readline());
var n = parseInt(readline());
var a = parseInt(readline());
console.log(Math.ceil(m/a) * Math.ceil(n/a));
}
