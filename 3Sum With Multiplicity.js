var threeSumMulti = function(arr, target) {
    var k;
    var result = 0
    for(var i=0; i < arr.length; i++){
        var count = Array(101).fill(0);
        for(var j=i+1; j < arr.length; j++){
            k = target - arr[i] - arr[j];
            if(k>=0 & k <= 100 & count[k] > 0){
                result += count[k];
                result = result % (10**9 + 7);
            }
            count[arr[j]] = count[arr[j]]+1;
        }
    }
    return result;
};

