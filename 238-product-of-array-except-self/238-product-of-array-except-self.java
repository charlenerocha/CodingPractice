class Solution {
    public int[] productExceptSelf(int[] nums) {
        int[] result=new int[nums.length];
        
        int mult=1;
        int ifZero=1;
        Boolean nonZero=false;
        int numZero=0;
        
        for(int i=0;i<nums.length;i++){
            mult=mult*nums[i];
            if(nums[i]!=0){
                nonZero=true;
                ifZero=ifZero*nums[i];
            }else{
                numZero++;
            }
        }
        
        for(int i=0;i<nums.length;i++){
            if(nums[i]==0&&numZero>1){
                result[i]=0;
            }else if(nums[i]==0&&nonZero){
                result[i]=ifZero;
            }else{
                result[i]=mult/nums[i];
            }
        }
        
        return result;
    }
}