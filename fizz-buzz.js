var fizzBuzz = function(n) {
    let output=[];
    for(let i=1; i<=n; i++){
        if(i%3===0 && i%5===0){
            output[i-1]='FizzBuzz';
        }else if(i%3===0){
            output[i-1]='Fizz';
        }else if(i%5===0){
            output[i-1]='Buzz'
        }else{
            output[i-1]=i.toString();
        }
        
    }
    return output;
};
