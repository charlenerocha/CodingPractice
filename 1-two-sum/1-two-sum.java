class Solution {
    public int[] twoSum(int[] num, int target) {
        int[] result=new int[2];
        Map<Integer, Integer> ma =new HashMap<Integer, Integer>();
        for(int i=0; i < num.length;i++){
            if(ma.containsKey(target-num[i])){
                result[0]=ma.get(target-num[i]);
                result[1]=i;
                return result;
            }
            ma.put(num[i],i);
        }
        return result;
    }
}