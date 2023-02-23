class Solution {
    public int[] productExceptSelf(int[] nums) {
        int n = nums.length;
        int[] left_to_right = new int[n];
        int[] right_to_left = new int[n];

        int running_prod = 1;
        for(int i = 0; i < n; i++){
            running_prod *= nums[i];
            left_to_right[i] = running_prod;
        }

        running_prod = 1;
        for(int i = n-1; i >= 0; i--){
            running_prod *= nums[i];
            right_to_left[i] = running_prod;
        }

        int[] result = new int[n];
        for(int i = 1; i < n-1; i++){
            result[i] = left_to_right[i-1] * right_to_left[i+1];
        }
        result[0] = right_to_left[1];
        result[n-1] = left_to_right[n-2];
        
        return result;
    }
}
