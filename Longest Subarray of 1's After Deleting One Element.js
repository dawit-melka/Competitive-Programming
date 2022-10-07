var longestSubarray = function(nums) {
    var left = 0;
    var right = 0;
    var move = 1;
    
    while(right < nums.length){
        if(nums[right] !== 1) move--;
        if(move < 0){
            if(nums[left] !== 1) move++;
            left++
        }
        right++;
    }
    return right-left-1;
};
