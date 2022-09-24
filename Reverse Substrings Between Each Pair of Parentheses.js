var reverseParentheses = function(s) {
    s = s.split('');
    var reversed = [];
    var temp = [];
    for(let c of s){
        if(c === ')'){
            var letter = reversed.pop();
            temp = []
            while(letter !== '('){
                temp.push(letter);
                letter = reversed.pop();
            }
            reversed = reversed.concat(temp);
        }else{
            reversed.push(c)
        }
    }
    return reversed.join('');
};
