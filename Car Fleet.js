var carFleet = function(target, position, speed) {
    var stack = [];

    position = position.map((p,i) => [p, speed[i]]); // pair position with corresponding time
    position.sort((a, b) => b[0] - a[0]); //sort from largest position
    
    for(var i=0; i < position.length; i++){
        stack.push((target - position[i][0])/position[i][1]); // push time required to destination
        if(stack.length > 1 & stack[stack.length -1] <= stack[stack.length-2]){ 
            stack.pop(); // if the current car time lower or equal prev fleet happens;
        }
    }
    return stack.length;
};
