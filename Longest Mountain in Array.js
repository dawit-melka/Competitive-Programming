var longestMountain = function(arr) {
    var prev = 0;
    var curr = 1;
    var max = 0;
    var count = 1;
    var direction = "up";
    
    while(curr < arr.length){
        
        if(arr[curr] > arr[prev] & direction === 'up'){
            count++;
        }else if(arr[curr]<arr[prev] & direction === 'up' & count > 1){
            count++;
            direction = 'down';
            max = Math.max(max, count);
        }else if(arr[curr]<arr[prev] & direction === 'down'){
            count++;
            max = Math.max(max, count);
        }else{
            if(arr[curr] > arr[prev]) count = 2;
            else count = 1;
            direction = 'up';
        }
        prev++;
        curr++;
    }
    return (max<3 ? 0 : max);
};
