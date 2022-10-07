var partitionLabels = function(s) {
    var last = {};
    var result = [];
    var end = 0;
    var start = 0;
    for(var i = 0; i < s.length; i++){
        last[s[i]] = i;
    }
    
    for(var i = 0; i < s.length; i++){
        end = Math.max(end, last[s[i]);
        
        if(end === i){
            result.push(end - start + 1);
            start = end +1;
        }
    }
    return result;
};
