var lengthOfLongestSubstring = function(s) {
    var map = new Map();
    var left = 0, right = 0, max=0;
    while(right < s.length){
        if(map.get(s[right])){
            map.set(s[right], map.get(s[right])+1)
            while(map.get(s[right])>1){
                map.set(s[left], map.get(s[left])-1);
                if(map.get(s[left]) === 0) map.delete(s[left]);
                left++;
            }
        }else map.set(s[right], 1);
        
        right++;
        max = Math.max(max, right-left)
    }
    return max;
};
