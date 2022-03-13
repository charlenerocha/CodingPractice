class Solution {
    public int[] twoSum(int[] num, int target) {
        int[] resultArray= new int[2];
        Map<Integer, Integer> map=new HashMap<Integer, Integer>();
        for(int i=0;i<num.length;i++){
            if(map.containsKey(target-num[i])){
                resultArray[0]=map.get(target-num[i]);
                resultArray[1]=i;
                return resultArray;
            }
            map.put(num[i], i);
        }
        return resultArray;
    }
}