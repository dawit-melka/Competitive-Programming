var furthestBuilding = function(heights, bricks, ladders) {
    const maxHeap = [];
    
    for (var i = 0; i < heights.length-1; i++) {
        if (heights[i] >= heights[i+1]) continue;
        let requiredBricks = heights[i+1] - heights[i];
        
        if (requiredBricks <= bricks) {
            bricks -= requiredBricks;
            add(requiredBricks);
        } else {
            if (ladders === 0) break;
            
            if (maxHeap [0] > requiredBricks) {
                bricks += poll();
                bricks -= requiredBricks;
                add (requiredBricks);
            } 
            ladders--;
        }
    }
    
    function add (val) {
        maxHeap.push(val);
        let index = maxHeap.length-1;
        //Bubble Up
        while (maxHeap[index] > maxHeap[Math.floor((index - 1) / 2)]) {
            maxHeap[index] = maxHeap[Math.floor((index - 1) / 2)];
            maxHeap[Math.floor((index - 1) / 2)] = val;
            index = Math.floor((index - 1) / 2);
        }
    }
    
    function poll () {
        let maxValue = maxHeap[0];
        maxHeap[0] = maxHeap.at(-1);
        maxHeap.pop();
        
        // Sinck Down
        let index = 0;
        while (maxHeap[index] < maxHeap[2*index + 1] 
              || maxHeap[index] < maxHeap[2*index + 2]) {
            let maxChildIndex = 2*index + 1;
            
            if (maxHeap[maxChildIndex] < maxHeap[2*index + 2]) {
                maxChildIndex = 2*index + 2;
            }
            
            let temp = maxHeap[index];
            maxHeap[index] = maxHeap[maxChildIndex];
            maxHeap[maxChildIndex] = temp;
            index = maxChildIndex;
        }
        return maxValue;
    }
    
    return i;
};
