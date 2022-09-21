var maxFrequency = function(nums, k) {
    
    nums.sort((a,b) => a-b)
    let start = 0
    let sum = 0
    let maxFreq = Math.max();
    
    for(let end = 0; end < nums.length; end++ ){
        sum += nums[end];
        
        while((end - start +1)*nums[end] > sum + k){
            sum -= nums[start++];
        }
        maxFreq = Math.max(maxFreq, end - start +1)
    }
    return maxFreq;
    
};
