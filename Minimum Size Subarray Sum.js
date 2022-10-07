var minSubArrayLen = function(target, nums) {
    var right = 0;
    var left = 0;
    var sum = 0;
    var minLen = Infinity;
    while(right <= nums.length){
        if(sum < target){
            sum+=nums[right];
            right++;
        }else {
            minLen = Math.min(minLen, right-left);
            sum -= nums[left];
            left++;
        }
        
    }
    return minLen === Infinity ? 0 : minLen;
};
