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
        if (head == null) { 
            return head; 
        }
        
        ListNode nextNode = head.next;
        ListNode current = head;
        ListNode prevNode = null;



        while (nextNode != null) {
            current.next = prevNode;
            prevNode = current;
            current = nextNode;
            nextNode = nextNode.next;
        }
        current.next = prevNode;
        return current;
    }
}
