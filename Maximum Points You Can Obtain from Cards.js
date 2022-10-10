var maxScore = function(cardPoints, k) {
    var total = 0;
    var n = cardPoints.length;
    var l = 0;
    var r = n - k;
    
    for(var i = n-k; i<n; i++){
        total += cardPoints[i];
    } 
    var result = total;
    
    while(r < n){
        total +=(cardPoints[l]-cardPoints[r]);
        result = Math.max(result, total);
        r++;
        l++;
    }
    return result;
};
