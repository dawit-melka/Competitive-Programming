var partitionLabels = function(s) {
    var last = Array(26).fill(0);
    var idx;
    var result = [];
    var end = 0;
    var start = 0;
    for(var i = 0; i < s.length; i++){
        idx = s[i].charCodeAt() - 97;
        last[idx] = i;
    }
    
    for(var i = 0; i < s.length; i++){
        idx = s[i].charCodeAt() - 97;
        end = Math.max(end, last[idx]);
        
        if(end === i){
            result.push(end - start + 1);
            start = end +1;
        }
    }
    return result;
};
