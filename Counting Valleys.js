'use strict';

const fs = require('fs');

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', function(inputStdin) {
    inputString += inputStdin;
});

process.stdin.on('end', function() {
    inputString = inputString.split('\n');

    main();
});

function readLine() {
    return inputString[currentLine++];
}

/*
 * Complete the 'countingValleys' function below.
 *
 * The function is expected to return an INTEGER.
 * The function accepts following parameters:
 *  1. INTEGER steps
 *  2. STRING path
 */

function countingValleys(steps, path) {
    // Write your code here
    
        
    var count = 0;
    var seaLevel = 0
    function check(step){
        
        if(step === "U"){
        seaLevel++;
        }else{
            seaLevel--;
        }
    }
    
    check(path[0]);
    for(let i=1; i<steps; i++){
        
        if(seaLevel < 0){
            
            check(path[i]) 
            if(seaLevel === 0) count++;    
        }else{
            check(path[i])
            }

        }

    return count;
}

function main() {
    const ws = fs.createWriteStream(process.env.OUTPUT_PATH);

    const steps = parseInt(readLine().trim(), 10);

    const path = readLine();

    const result = countingValleys(steps, path);

    ws.write(result + '\n');

    ws.end();
}
