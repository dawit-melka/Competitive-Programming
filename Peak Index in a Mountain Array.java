class Solution {
    public int peakIndexInMountainArray(int[] arr) {
        int left = -1;
        int right = arr.length;

        while (right > left + 1){
            int mid = left + (int)Math.floor((right - left) / 2);
            if(arr[mid] > arr[mid+1] && arr[mid] > arr[mid-1])
                return mid;
            else if(arr[mid] > arr[mid+1])
                right = mid;
            else
                left = mid;
        }
        return right;
    }
}
