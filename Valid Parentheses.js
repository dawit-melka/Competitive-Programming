var isValid = function(s){
    var map = {
        ')' : '(',
        '}' : '{',
        ']' : '['
    };
    var stack = [];
    for(let p of s){
        if(['(', '{', '['].includes(p))stack.push(p);
        else{
            if(map[p] !== stack.pop()) return false;
        }
    }
    return stack.length === 0;
};
