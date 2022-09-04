/**
 * @param {number[][]} intervals
 * @return {number[][]}
 */
var merge = function(intervals) {
    
    // bubble sort
    let j=0;
    let noSwap = true;
    for(let i=intervals.length; i>0; i--){
        noSwap=true
        for(let j=0; j<i-1; j++){
            if(intervals[j][0] > intervals[j+1][0]){
                let temp = intervals[j]
                intervals[j] = intervals[j+1];
                intervals[j+1] =temp;
                noSwap = false;
            }
        }
        if(noSwap) break;
    }
    
    let merged =[intervals[0]];
    
    for(let i=1; i<intervals.length; i++){
        if(merged[j][1] >= intervals[i][0] || merged[j][1] >= intervals[i][1]){
            if(merged[j][1] < intervals[i][1]){
            merged[j]=[merged[j][0],intervals[i][1]]
            }
            
        }else{
            merged.push(intervals[i])
            j++;
        }
    }
    return merged
    
};
