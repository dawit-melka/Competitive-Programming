var removeKdigits = function(num, k) {
    if(num.length === k) return "0";
    var stack=[];
    for(var x of num){
        
        while(stack.length && k && x < stack[stack.length-1] ){
            stack.pop();
            k--;
        }
        if(stack.length || x==0) stack.push(x);
    }
    while(k){
        stack.pop();
        k--;
    }
    return !stack.length? "0" : stack.join('');
};
