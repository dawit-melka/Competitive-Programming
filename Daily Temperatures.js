var dailyTemperatures = function(temperatures) {
    var stack = [], 
        result = new Array(temperatures.length).fill(0);
    for(var i=temperatures.length-1; i>=0; i--){
        while(stack.length && temperatures[i]>=temperatures[stack[stack.length-1]]){
            stack.pop();
        }
        if(stack.length){
            result[i] = stack[stack.length-1] - i;
        }
        stack.push(i);
    }
    return result;
};
