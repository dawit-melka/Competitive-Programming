var isPalindrome = function(s) {
    var replaced = s.toLowerCase().replace(/[^a-z0-9]/gi,'')
 
    for(var l=0, r=replaced.length-1; l < r; l++, r--){
        if(replaced[l] !== replaced[r]) return false;
    }
    return true;
};
