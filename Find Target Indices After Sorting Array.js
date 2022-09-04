/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var targetIndices = function(nums, target) {
    
    var targetIndices=[]
    let noSwap =true;
    for(let i=nums.length; i>0; i--){
        noSwap =true;
        for(let j=0; j<i-1; j++){
            if(nums[j] > nums[j+1]){
                let temp = nums[j];
                nums[j] = nums[j+1];
                nums[j+1]=temp;
                noSwap = false;
            }
        }
        if(noSwap) break;
    }
    
    for(let i=0; i<nums.length; i++){
        if(nums[i]===target) targetIndices.push(i);
    }
    return targetIndices;
    
    
};
