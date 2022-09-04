/**
 * @param {number[]} nums
 * @return {number[]}
 */
var smallerNumbersThanCurrent = function(nums) {
    
    var output=[]
    //merge sort
    function merge(arr1, arr2){
        
        var result=[]
        var i=0;
        var j=0;
        while(i<arr1.length && j<arr2.length){
            if(arr1[i]<arr2[j]){
                result.push(arr1[i]);
                i++;
            }else{
                result.push(arr2[j])
                j++;
            }
            if(arr1.length === i) result=result.concat(arr2.slice(j));
            if(arr2.length === j) result = result.concat(arr1.slice(i));
        }
        return result;
    }
    
    function mergeSort(arr){
        
        if(arr.length <= 1) return arr;
        var mid = Math.floor(arr.length/2);
        
        var left = mergeSort(arr.slice(0,mid));
        var right = mergeSort(arr.slice(mid));
        
        return merge(left, right);
    }
    
    let sortedArr = mergeSort(nums);
    
    for(let i=0; i <nums.length; i++){
        output.push(sortedArr.indexOf(nums[i]))
    }
    return output;
    
};
