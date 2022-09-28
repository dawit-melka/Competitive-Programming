var lengthOfLongestSubstring = function(s) {
    var seen = new Map();
    var start = 0, max = 0;
    for(let i=0; i<s.length; i++){
        if(seen.has(s[i])) start = Math.max(seen.get(s[i])+1, start);
        seen.set(s[i], i);
        max = Math.max(max, i-start+1)
    }
    return max;
};
