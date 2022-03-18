class Solution {
    public boolean isAnagram(String s, String t) {
        //convert into array, compare by index
        char[] sA= s.toCharArray();
        char[] tA=t.toCharArray();
        
        //sort array for ordered comparison
        Arrays.sort(sA);
        Arrays.sort(tA);
        
        return (Arrays.equals(sA,tA));
        
        
    }
}