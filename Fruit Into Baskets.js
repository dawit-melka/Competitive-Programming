var totalFruit = function(fruits) {
    var map = new Map();
    var right = 0;
    var left = 0;
    
    while(right < fruits.length){
        if(map.get(fruits[right])) map.set(fruits[right], map.get(fruits[right])+1);
        else map.set(fruits[right], 1);
        
        if(map.size > 2){
            if(map.get(fruits[left]) === 1) map.delete(fruits[left]);
            else map.set(fruits[left], map.get(fruits[left])-1);
            left++;
        }
        right++;
    }
    return right-left;
};
