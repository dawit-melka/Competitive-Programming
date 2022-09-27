var rotate = function(nums, k) {
    var n = nums.length;
    k = k % n;
    var movable_index = k;
    var visited = 0;
    var intial_index = 0;
    var movable_variable = nums[0];
    while(visited < n) {
            
        var temp = nums[movable_index];
        nums[movable_index] = movable_variable;
        movable_variable = temp;
            
        if(movable_index === intial_index) {
            intial_index = (movable_index+1) % n;
            movable_index = intial_index;
            movable_variable = nums[intial_index];
            }
            
        movable_index = (k+movable_index) % n;
        visited++;
        }
};
