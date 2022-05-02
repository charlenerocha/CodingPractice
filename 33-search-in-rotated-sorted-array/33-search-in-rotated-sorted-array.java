class Solution {
    public int search(int[] nums, int target) {
        if(nums.length-nums[0]<nums.length-nums[0]+target){
            for(int i=0;i<nums.length;i++){
                if(nums[i]==target){
                    return i;
                }
            }
        }else{
            for(int i=nums.length-1;i>=0;i--){
                if(nums[i]==target){
                    return i;
                }
            }
        }
        
        
        
        return -1;
    }
}