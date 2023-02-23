class Solution {
    public int minSubArrayLen(int target, int[] nums) {
        int result = nums.length;
        int window_sum = 0;
        int left = 0;
        boolean has_sub_array = false;
        
        for(int right = 0; right < nums.length; right++){
            window_sum += nums[right];
            while(window_sum >= target){
                has_sub_array = true;
                result = Math.min(result, right - left + 1);
                window_sum -= nums[left];
                left++;
            }
        }
        
        
        return has_sub_array? result : 0;
    }
}
