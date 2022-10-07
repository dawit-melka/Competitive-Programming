const subarraySum = (nums, k) => {
	var map = {0:1};
    var count = 0;
    var sum = 0;
    
    for(var x of nums){
        sum += x;
        if(map[sum-k]) count+=map[sum-k];
        map[sum] = (map[sum] || 0) + 1;
    }
    return count;
};
