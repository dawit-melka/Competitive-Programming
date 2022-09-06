var rearrangeArray = function(nums) {
    
    var sorted = nums.sort((a,b) => a-b);
    
    var left=0;
    var right = sorted.length - 1
    
    if((sorted.length-1)%2 ===0) {
        var right = sorted.length -2;
    }
        
    
    while(left<right){
        let temp = sorted[left]
        sorted[left] = sorted[right]
        sorted[right] = temp;
        left += 2;
        right -= 2;
    }
    
    return sorted  
    
};
