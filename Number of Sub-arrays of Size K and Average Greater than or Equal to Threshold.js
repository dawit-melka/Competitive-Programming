var numOfSubarrays = function(arr, k, threshold) {
    var thresholdSum = k * threshold;
    var sum = 0;
    var count = 0;
    var left = 0;
    for(var right = 0; right <= arr.length; right++){
        
        if(right >= k){
            if(sum >= thresholdSum) count++;
            sum -= arr[left];
            left++;
        }
        sum += arr[right];
    }
    return count;
};
