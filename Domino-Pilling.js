const fs = require('fs');
const input = fs.readFileSync(0,'utf8').trim().split('\n');
 
let currentLine = 0;
function readline(){
    return input[currentLine++];
}
 
let [M, N] = readline().split(' ').map(x=>+x);
console.log(Math.floor(M*N/2));
