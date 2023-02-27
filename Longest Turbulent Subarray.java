class Solution {
    public int maxTurbulenceSize(int[] arr) {
        int result = 1;
        int left = 0;
        int right = 1;

        while (right < arr.length){
            while(right < arr.length && arr[right] == arr[right-1]){
                left = right;
                right++;
            }
            if(right == arr.length)
                break;
            boolean isGreater = arr[right] > arr[right-1];
            while(right < arr.length){
                if(arr[right] == arr[right-1] ||
                    isGreater && arr[right] < arr[right-1] ||
                    !isGreater && arr[right] > arr[right-1])
                    break;

                isGreater = !isGreater;
                right++;
            }
          result = Math.max(result, right - left);
          left = right-1;
        }
        return result;
    }
}
