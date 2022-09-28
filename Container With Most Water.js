var maxArea = function(height) {
    var max = 0;
    var right = height.length-1;
    var left = 0;
    var area;
    while(left < right){
        area = Math.min(height[right], height[left]) * (right-left);
        if(height[right] > height[left]) left++;
        else right--;
        max = Math.max(area, max);
    }
    return max;
};
