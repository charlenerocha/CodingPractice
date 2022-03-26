/**
 * Definition for singly-linked list.
 * class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    public boolean hasCycle(ListNode head) {
        HashSet<ListNode> trackNodes = new HashSet<ListNode>();
        while(head!=null){
            if(trackNodes.contains(head)){
                return true;
            }
            trackNodes.add(head);
            head=head.next;
        }
        return false;
    }
}