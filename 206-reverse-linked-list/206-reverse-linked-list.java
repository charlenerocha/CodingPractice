/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode reverseList(ListNode head) {
        if (head==null) return null;
        
        ListNode hold=head.next;
        ListNode myList=new ListNode(head.val);
        
        while(hold!=null){
            ListNode temp=myList;
            ListNode holdNode=new ListNode(hold.val);
            
            myList=holdNode;
            myList.next=temp;
            
            hold=hold.next;
        }
        
        return myList;
    }
}