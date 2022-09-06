/**
 * @param {string[]} nums
 * @param {number} k
 * @return {string}
 */
var kthLargestNumber = function(nums, k) {
    
    function merge(arr1, arr2){
	    var result =[];
  	  var i=0;
  	  var j=0;
  	while(i<arr1.length && j<arr2.length){
    	if(arr1[i] - arr2[j] > 0){
    	    result.push(arr1[i]);
    	    i++;
    	   	}else{
    	        result.push(arr2[j])
    	        j++;
    	}
    	if(arr1.length === i) result=result.concat(arr2.slice(j));
    	if(arr2.length === j) result=result.concat(arr1.slice(i));
    }
    return result;
}

function mergeSort(arr){
    if(arr.length<=1) return arr;
    var mid=Math.floor(arr.length/2)
    var left=mergeSort(arr.slice(0,mid));
    var right=mergeSort(arr.slice(mid));
    return merge(left,right);
}
    nums =nums.map(BigInt);
    var sorted =mergeSort(nums)
    
    return sorted[k-1] + "";
};
