class Solution {
    
    public int insertionIndex(int[] nums, int target, boolean left){
        int low = 0;
        int high = nums.length;
        while(low < high){
            int mid = (low + high) / 2;
            if (nums[mid] > target || (left && target == nums[mid])){
                high = mid;
            }else{
                low = mid + 1;
            }
        }
        
        return low;
    }
    
    public int[] searchRange(int[] nums, int target) {
        int[] targetRange = {-1,-1};
        
        int leftIdx = insertionIndex(nums, target, true);
        
        if (leftIdx == nums.length || nums[leftIdx] != target){
            return targetRange;
        }
        
        targetRange[0] = leftIdx;
        targetRange[1] = insertionIndex(nums, target, false) - 1;
        
        return targetRange;
    }
}