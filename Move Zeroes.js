var moveZeroes = function(nums) {
    
    var start=0;
    var end=1;
    
    while(end<nums.length){
          if(nums[start]===0 && nums[end]!==0){
              nums[start]=nums[end];
              nums[end]=0;
              start++;  
          }else if(nums[start]!==0) start++;
        end++
    }
 };
