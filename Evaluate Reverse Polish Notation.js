var evalRPN = function(tokens) {
    var stack = [];
    var calculate = {
        '+': function (x, y) { stack.push(y + x)},
        '-': function (x, y) { stack.push(y - x)},
        '*': function (x, y) { stack.push(y * x)},
        '/': function (x, y) { stack.push(parseInt(y / x))}
    };
    for(let op of tokens){
        if(['+', '*', '-', '/'].includes(op)) calculate[op](stack.pop(), stack.pop());
        else stack.push(parseInt(op));
    }
    return stack[0]
};
