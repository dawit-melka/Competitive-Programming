var nextPermutation = function(nums){
    
    // Find the first decreasing index moving from end to start (the last peak)
    for(var i=nums.length-1; i>=0; i--){
        if(nums[i] < nums[i+1]){
            const large = nextLarge(i); // find next larger from end to i 
            swap(large,i); // swap with it
            reverse(i+1); // reverse from i+1 to end
            return;
        }
    }
    // if it is decreasing order reverse
    nums.reverse();
 
    function swap(i,j){
        [nums[i],nums[j]] = [[nums[j]],[nums[i]]]
    }
    
    function reverse(idx){
        var start = idx;
        var end = nums.length-1
        while(start < end){
            swap(start, end)
            start++;
            end--;
        }
    }
    // looks for the larger than nums[i] from end to i-1
    function nextLarge(idx){
        for(var i= nums.length-1; i>idx; i--){
        if(nums[i] > nums[idx]){
            return i;
            }
        }
    }
}
