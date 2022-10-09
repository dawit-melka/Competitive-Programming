var maxSumTwoNoOverlap = function(nums, firstLen, secondLen) {
    var firstSum = [];
    var secondSum = [];
    var currSumF = 0;
    var currSumS = 0;
    var ans = 0;
    
    for(var i=0; i<nums.length; i++){
        currSumF+= nums[i];
        currSumS+= nums[i];
        if(i-firstLen+1 >=0){
            firstSum.push(currSumF);
            currSumF -= nums[i-firstLen+1];
        }
        if(i-secondLen+1 >=0){
            secondSum.push(currSumS)
            currSumS -= nums[i-secondLen+1];
        }
    }
    for(var i=0; i<firstSum.length; i++){
        for(var j=i+firstLen; j<secondSum.length; j++){
            currSumF = firstSum[i] + secondSum[j];
            ans = Math.max(ans, currSumF);
        }
    }
    for(var i=0; i<secondSum.length; i++){
        for(var j=i+secondLen; j<firstSum.length; j++){
            currSumS = secondSum[i] + firstSum[j];
            ans = Math.max(ans, currSumS);
        }
    }
    return ans;
};
