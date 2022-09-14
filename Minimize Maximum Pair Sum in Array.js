var minPairSum = function(nums) {
    nums.sort((a,b) => a-b)
    let max=-Infinity;
    let left =0
    let right = nums.length - 1;
    while(left<right){
        max = Math.max(max, nums[left] + nums[right])
        left++;
        right--;
    }
    return max;
};
