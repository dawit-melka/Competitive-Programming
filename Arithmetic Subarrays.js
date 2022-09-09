var checkArithmeticSubarrays = function(nums, l, r) {
    
    let subArrays = [];
    let result = []
    
    for(let i=0; i<l.length; i++){
        
        subArrays.push(nums.slice(l[i], r[i] +1).sort((a,b) => a-b))
    }
    
    for(let i=0; i<subArrays.length; i++){
        
        let gap = subArrays[i][1] - subArrays[i][0];
        let arithmetic = true;
        for(let j=1; j<subArrays[i].length - 1; j++){
            
            let nextGap = subArrays[i][j+1] - subArrays[i][j];
            
            if(gap !== nextGap){
                arithmetic = false;
                break;
            }
        }
        result.push(arithmetic)
    }
    
    return result;
    
};
