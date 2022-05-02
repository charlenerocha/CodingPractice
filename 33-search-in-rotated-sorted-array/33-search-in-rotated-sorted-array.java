class Solution {
    public int search(int[] nums, int target) {
        // boolean rev=false;
        // if(nums[0]<nums.length){
        //     rev=true;
        // }
        
        for(int i=0;i<nums.length;i++){
            if(nums[i]==target){
                return i;
            }
        }
        
        return -1;
    }
}