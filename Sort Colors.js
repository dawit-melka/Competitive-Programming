/**
 * @param {number[]} nums
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var sortColors = function(nums) {
    let noSwap=true;
    
    for(let i=nums.length; i>0; i--){
        noSwap = true;
        for(let j=0; j<i-1; j++){
            if(nums[j] > nums[j+1]){
                let temp = nums[j];
                nums[j] = nums[j+1]
                nums[j+1] = temp;
                noSwap = false
            }
        }
        if(noSwap) break;
    }
    return nums;
};
