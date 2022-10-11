var xorQueries = function(arr, queries) {
    var result = [];
    
    for(i=1; i<arr.length; i++){
        arr[i] = arr[i-1] ^ arr[i];
    }
   
    for(var q of queries){
        var l = q[0];
        var r = q[1];
        if(l === 0) result.push(arr[r]);
        else result.push(arr[r]^arr[l-1])
    }
    return result;
};
