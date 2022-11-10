var decodeString = function(s) {
    let stack = [];
    for(let char of s){
        if(char !==']'){
            stack.push(char);
            continue;
        }
        
        let curr = '';
        // pop and concat every alphabet charactes
        while(stack.length && stack[stack.length-1]!== '['){
            curr = stack.pop() + curr;
        }
        stack.pop(); // removes '['
        
        let count = '';
        // pop every number characters concat
        while(stack.length && /[0-9]/.test(stack[stack.length-1])){
            count = stack.pop() + count;
        } 
        curr = curr.repeat(+count);
        stack.push(curr);
    }
    return stack.join('');
};


