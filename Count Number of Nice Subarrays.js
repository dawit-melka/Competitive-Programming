var numberOfSubarrays = function(nums, k) {
    var map = {0 : 1};
    var sum = 0;
    var count = 0;
    
    for(var n of nums){
        sum += n%2;
        if(map[sum-k]) count += map[sum-k];
        map[sum] = (map[sum] || 0) +1;
    }
    return count;
};
