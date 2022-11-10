var findKthLargest = function(nums, k) {
    let pivot, pivotIdx;
    let finalIdx = nums.length -k
    let start = 0;
    let end = nums.length-1;
    while(start <= end){
        pivot = Math.floor(Math.random()*(end-start+1)) +start;
        pivotIdx = pivotHelper(pivot, start, end);
        
        if(pivotIdx === finalIdx) return nums[pivotIdx];
        if(pivotIdx > finalIdx) end = pivotIdx-1;
        else start = pivotIdx+1;
    }
    
    function pivotHelper(pivot, start, end){
        let pivotVal = nums[pivot];
        swap(pivot, end);
        let i = 0;
        for(let j = 0; j < end; j++){
            if(nums[j] <= pivotVal){
                swap(i,j);
                i++;
            }
        }
        swap(i, end);
        return i;
    }
    
    function swap(i, j){
        let temp = nums[i];
        nums[i] = nums[j];
        nums[j] = temp
    }
};
