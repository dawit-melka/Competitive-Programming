var minimumBuckets = function(streets) {
    var s = [...streets]
    var cnt = 0;
    for(var i=0; i<s.length; i++){
        if(s[i] === 'H'){
            if(s[i-1] === 'B') continue;
            if(s[i+1] === '.'){
                s[i+1] = 'B';
                cnt++;
                continue;
            }
            if(s[i-1] === '.'){
                s[i-1] = 'B';
                cnt++;
                continue;
            }
            else return -1;
        }
    }
    return cnt;
};
