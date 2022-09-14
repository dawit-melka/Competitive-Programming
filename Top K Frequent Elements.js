var topKFrequent = function(nums, k) {
    
    let freq ={}
    
    for(let val of nums) freq[val]=(freq[val] || 0)+1;
    
    freq = Object.keys(freq).sort((a,b)=>freq[b]-freq[a]).map(Number)
    
    return freq.slice(0,k);
    
};
