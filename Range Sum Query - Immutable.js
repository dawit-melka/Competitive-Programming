var NumArray = function(nums) {
        this.nums = nums
        for(let i=1; i<nums.length; i++) this.nums[i]=this.nums[i] + this.nums[i-1];
};

NumArray.prototype.sumRange = function(left, right) {
    if(left === 0) return this.nums[right];
    else return this.nums[right] - this.nums[left-1];
};
