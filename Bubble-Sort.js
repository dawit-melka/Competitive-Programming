'use strict';

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
 * Complete the 'countSwaps' function below.
 *
 * The function accepts INTEGER_ARRAY a as parameter.
 */

function countSwaps(a) {
    // Write your code here
    let swap=0
    var noSwap=true;
    for(let i=a.length; i>0; i--){
        noSwap=true
        for(let j=0; j<a.length; j++){
            if(a[j]>a[j+1]){
                let temp=a[j];
                a[j] = a[j+1];
                a[j+1] = temp;
                swap++;
                noSwap=false
            }
        }
        if(noSwap) break;
    }
    console.log("Array is sorted in "+swap+" swaps.")  
    console.log("First Element: "+a[0])  
    console.log("Last Element: "+a[a.length-1])  

}

function main() {
    const n = parseInt(readLine().trim(), 10);

    const a = readLine().replace(/\s+$/g, '').split(' ').map(aTemp => parseInt(aTemp, 10));

    countSwaps(a);
}
