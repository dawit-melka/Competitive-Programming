var maxVowels = function(s, k) {
    
    var vowels = new Set(['a','e','i','o','u']);
    var count = 0;
    var left = 0;
    var max = 0;
    
    for(var right=0; right < s.length; right++){
        if(vowels.has(s[right])){
            count++; 
        } 
        if(right - left >= k){
            if(vowels.has(s[left])) count--;
            left++; 
        };
        max = Math.max(max, count);
    }
    return max;
};
