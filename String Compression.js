var compress = function(chars) {
    if(chars.length < 2) return chars.length;
    var start = 0;
    var end = start;
    var count = 0;
    while(end <= chars.length){
        
        if(chars[start] !== chars[end]){
            if(count !== 1){
                count = count.toString();
                for(let i=0; i<count.length; i++){
                    chars[++start] = count[i];
                }
            } 
            chars[++start] = chars[end];
            count = 0;
        }
        count++;
        end++;
    }
    return start;
};
