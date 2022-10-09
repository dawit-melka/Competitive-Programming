var longestSubarray = function(nums, limit) {
    var s = 0,
        e = 0,
        ans = 0,
        maxQueue = [],// decreasing order
        minQueue = []; // increasing order
    while(e < nums.length){
        var x = nums[e];
        // pop all the elements less than x to keep the decreasing order

        while(maxQueue.length && x >= nums[maxQueue[maxQueue.length-1]]){ 
            maxQueue.pop();
        }
        maxQueue.push(e); 
        // pop all the elements greater than x to keep the increasing order
        while(minQueue.length && x <= nums[minQueue[minQueue.length-1]]){ 
            minQueue.pop();                                         
        }
        minQueue.push(e);
        
        var max = nums[maxQueue[0]];
        var min =  nums[minQueue[0]];
        // if the difference is greater than the limit
        if(max - min > limit){
            s++;  // increment the start index
            if(s > maxQueue[0]) maxQueue.shift(); // remove all the indices before s
            if(s > minQueue[0]) minQueue.shift();
        }else {
            // console.log(s,e);
            ans = Math.max(ans, e-s+1); //maximize the answer
            e++; // increment the end index
        }
    }
    return ans;
};
