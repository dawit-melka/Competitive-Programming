var isPowerOfThree = function(n) {
    if(n === 1) return true;
    if(n%3 !== 0 || n <= 0) return false;
    
    n = n/3;
    return isPowerOfThree(n)
};
