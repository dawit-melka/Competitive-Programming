var validateStackSequences = function(pushed, popped) {
    var stack = [pushed[0]];
    var i=1;
    var j=0;
    while(i < pushed.length || j < popped.length){
        if(i===pushed.length & stack[stack.length-1] !== popped[j]) return false;
        if(stack[stack.length-1] === popped[j]){
            stack.pop();
            j++;
        }else stack.push(pushed[i++]);
    }
    return true
};
