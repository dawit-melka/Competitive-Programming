var maxCoins = function(piles) {
    
    piles.sort((a,b) => a-b);
    let count=0;
    let output=0;
    let index = piles.length -2
    while(count < piles.length/3){
        output+=piles[index]
        index-=2
        count++
    }
    
    return output;
    
};
