var productExceptSelf = function(nums) {
    var prefix = 1;
    var postfix = 1;
    var result = [1];
    for(let i=0; i<nums.length; i++){
        result[i] = prefix;
        prefix *= nums[i];
    }
    for(let i=nums.length-1; i>=0; i--){
        result[i] *= postfix;
        postfix *= nums[i];
    }
    return result;
};
