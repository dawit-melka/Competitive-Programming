var nextGreaterElement = function(nums1, nums2) {
    var output = [];
    let indx;
    let nextGreater;
    for(let x of nums1){
        indx = nums2.indexOf(x);
        nextGreater = -1;
        for(let i=indx+1; i<nums2.length; i++){
            if(nums2[i] > x){
                nextGreater = nums2[i];
                break;
            }
        }
        output.push(nextGreater);
    }
    return output
};
