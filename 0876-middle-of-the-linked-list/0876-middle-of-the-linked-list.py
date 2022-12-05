# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        p=q=head

        while q.next !=None:
            p=p.next 
            if q.next.next:
                q=q.next.next
            else:
                break
        return p