var maxOperations = function(nums, k) {
    
    let frequencyCounter ={};
    let counter = 0
    
    for(let val of nums){
        frequencyCounter[val] =(frequencyCounter[val] || 0) +1;
    }
    
    for(let val of nums){
        let complement = k - val;
        if(frequencyCounter[val] === 0){
            continue;
        }
        frequencyCounter[val] -=1
        if(frequencyCounter[complement] >= 1){
            frequencyCounter[complement] -=1;
            counter++
            
        }
    }
    
    return counter;
   
    
};
