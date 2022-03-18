class Solution {
    public boolean isValid(String s) {
        Stack<Character> sStack=new Stack<Character>();
        
        for(int i=0;i<s.length();i++){
            if(s.charAt(i)=='('){
                sStack.push(')');
            }else if(s.charAt(i)=='{'){
                sStack.push('}');
            }else if(s.charAt(i)=='['){
                sStack.push(']');
            }else if(sStack.empty()==true){
                return false;
            }else if(s.charAt(i)!=sStack.peek()){
                return false;
            }else{
                sStack.pop();
            }
        }
        
        return sStack.empty();
    }
}