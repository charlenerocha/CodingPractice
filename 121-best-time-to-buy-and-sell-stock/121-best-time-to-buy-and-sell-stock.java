//sliding window technique
class Solution {
    public int maxProfit(int[] prices) {
        int left=0;
        int right=1;
        int maxProf=0;
        
        while(left<right && right<prices.length){
            int curProf=prices[right]-prices[left];
            
            if(prices[left]<prices[right]){
                maxProf=Math.max(curProf,maxProf);
            }else{
                left=right;
            }
            
            right++;
        }
        
        return maxProf;
    }
}