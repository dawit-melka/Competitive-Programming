class Solution {
    public int[] nextGreaterElements(int[] nums) {
        ArrayList<Integer> stack = new ArrayList<>();
        int[] nge = new int[nums.length];

        for(int i = 0; i < nums.length; i++){
            while(stack.size() > 0 && nums[i] > nums[stack.get(stack.size()-1)]){
                nge[stack.remove(stack.size()-1)] = nums[i];
            }
            stack.add(i);
        }
        
        for(int i = 0; i < nums.length; i++){ 
            while(stack.size() > 0 && nums[i] > nums[stack.get(stack.size() - 1)]){
                int curr_idx = stack.remove(stack.size()-1);
                nge[curr_idx] = nums[i];
            }
        }

        while(stack.size() > 0){
            int curr_idx = stack.remove(stack.size()-1);
            nge[curr_idx] = -1;
        }

        return nge;
    }
}
