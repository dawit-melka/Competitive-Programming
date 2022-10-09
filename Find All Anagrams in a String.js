var findAnagrams = function(s, p) {
    var map = {};
    var count = 0;
    var ans=[];
    
    for(var c of p){
        map[c]=(map[c] || 0) +1;
    };
    
    for(var i=0; i<s.length; i++){
        if(map.hasOwnProperty(s[i])) {
            count++;
            map[s[i]]-=1;
            if(map[s[i]] < 0) count--;
        }else count--;
        
        if(count === p.length) ans.push(i-p.length+1);
        
        if(i-p.length+1 >= 0){
            if(map.hasOwnProperty(s[i-p.length+1])){
                count--;
                map[s[i-p.length+1]] += 1;
                if(map[s[i-p.length+1]] <= 0) count++;
            }else count++;
        } 
    }
    return ans;
};
