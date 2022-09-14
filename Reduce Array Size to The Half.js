var minSetSize = function(arr) {
    
    let frequency = {}
    let values =[]
    let half = arr.length/2
    let sum=0
    
    for(let val of arr){
        frequency[val]=(frequency[val] || 0) +1
    }
    values= Object.values(frequency)
    values.sort((a,b)=> b-a);
    
    for(var i=0; i<values.length; i++){
        sum += values[i]
        if(sum>=half) break;
    }
    return i+1;
    
};
