var pivotIndex = function(nums) {
   
   var prefixSum =[nums[0]]
   for(let i=1; i<nums.length; i++){
       prefixSum[i] = nums[i] + prefixSum[i-1]; 
   }
    for(let i=0; i<nums.length; i++){
        let rightSum = prefixSum[i] - nums[i];
        let leftSum = prefixSum[nums.length-1] - prefixSum[i]
        if(rightSum === leftSum) return i;
    }
    return -1;
};
