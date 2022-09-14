var pancakeSort = function(arr) {
    let max = arr.length;
    let k = [];
    while(max>1){
        
        flip(arr.indexOf(max));
        max--;
    }
    function flip(indx){
        if(indx){
            for(let i=0; i<indx/2; i++){
                [[arr[i], arr[indx-i]] = [arr[indx-i], arr[i]]]
            };
            k.push(indx+1)
        }
        let len=max-1;
        for(let i=0; i<len/2; i++){
            [[arr[i], arr[len-i]] = [arr[len-i], arr[i]]]
        };
        k.push(max)
    }
    return k;
    
};

