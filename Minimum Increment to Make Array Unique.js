var minIncrementForUnique = function(nums) {
    nums.sort((a,b) => a - b);
    var ans = 0;
    var inc = 0
    for(var i=1; i<nums.length; i++){
        if(nums[i] <= nums[i-1]){
            inc = nums[i-1] - nums[i] +1;
            nums[i]+= inc;
            ans += inc;
        }
    }
    return ans
};
