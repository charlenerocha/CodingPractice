class Solution {
    public int maxProfit(int[] prices) {
        int highestVal=0;
        int lowestVal=prices[0];
        
        for(int i=0;i<prices.length;i++){
            if(prices[i]>lowestVal){
                highestVal=Math.max(highestVal,prices[i]-lowestVal);
            }else{
                lowestVal=prices[i];
            }
        }	     
	    return  highestVal ;
	 }
}