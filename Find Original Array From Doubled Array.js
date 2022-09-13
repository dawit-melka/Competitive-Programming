var findOriginalArray = function(changed) {
    
    let map = new Map();
    let original = [];
    changed.sort((a,b) => a-b)
    
    for(let val of changed){
        let half = val/2;
        if(map.has(half) && map.get(half) > 0){
            original.push(half);
            map.set(half, map.get(half)-1);
        }else{
            map.set(val, map.has(val) ? map.get(val)+1 : 1)
        }
    }
    
    return original.length == changed.length/2 ? original : [];
    

};
