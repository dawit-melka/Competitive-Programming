var bagOfTokensScore = function(tokens, power) {
    var maxScore = 0;
    var score = 0;
    var right = tokens.length -1;
    var left = 0;
    tokens.sort((a,b) => a - b);
    while(left <= right){
        if(tokens[left] <= power){
            power -= tokens[left];
            left++;
            score++;
            maxScore = Math.max(maxScore, score);
        }else if(score > 0){
            power += tokens[right];
            right--;
            score--;
        }else break;
    }
    return maxScore;
};
