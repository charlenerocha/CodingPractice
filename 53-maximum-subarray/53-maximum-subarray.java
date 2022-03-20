class Solution {
    public int maxSubArray(int[] nums) {
        int currentMax=nums[0];
        int prevArray=nums[0];
        
        for(int i=1;i<nums.length;i++){
            prevArray=Math.max(prevArray+nums[i],nums[i]);
            currentMax=Math.max(prevArray, currentMax);
        }
        
        return currentMax;
    }
}