/**
 * @param {number[]} nums
 * @return {string}
 */
var largestNumber = function(nums) {
    
    for(let i=0; i<nums.length; i++){
        nums[i] = nums[i].toString();
    }
    
    
    let noSwap =true
    for(let i=nums.length; i>0; i--){
        noSwap = true;
        for(let j=0; j<i-1; j++){
            if(nums[j]+nums[j+1] < nums[j+1] + nums[j]){
                
                let temp =nums[j];
                nums[j] = nums[j+1]
                nums[j+1] = temp;
                noSwap=false;
            }
        }
        if(noSwap) break;
        
    }
    
    
    return nums[0] == 0? '0' : nums.join("");
    
    
};
