/**
 * @param {number[][]} points
 * @param {number} k
 * @return {number[][]}
 */
var kClosest = function(points, k) {
    
    if(points.length === k) return points;
    
    let noSwap = true;
    
    let distance = [];
    for(let i=0; i<points.length; i++){
        distance.push(Math.sqrt(Math.pow(points[i][0],2) + Math.pow(points[i][1],2)))
    }
    // distance.sort((a, b) => a - b);
    
    // console.log(distance);
    for(let i=points.length; i>0; i--){
        noSwap = true;
        for(let j = 0; j<i-1; j++){
            if(distance[j]>distance[j+1]){
                let temp1 =distance[j]
                distance[j] =distance[j+1]
                distance[j+1] = temp1;
                let temp2 = points[j];
                points[j] = points[j+1];
                points[j+1] = temp2;
                noSwap =false
            }
        }
        if(noSwap) break;
    }
    
    // points = points.slice(0,k)
    return points.slice(0,k)
    
};
