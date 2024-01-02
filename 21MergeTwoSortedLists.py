# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2:
            return

        headNode = ListNode()
        currentNode = headNode
        

        currentLeft = list1
        currentRight = list2

        while currentLeft and currentRight:
            if currentLeft.val < currentRight.val:
                currentNode.next = ListNode(currentLeft.val)
                currentLeft = currentLeft.next
            else:
                currentNode.next = ListNode(currentRight.val)
                currentRight = currentRight.next
            currentNode = currentNode.next
        
        while currentLeft:
            currentNode.next = ListNode(currentLeft.val)
            currentLeft = currentLeft.next
            currentNode = currentNode.next

        while currentRight:
            currentNode.next = ListNode(currentRight.val)
            currentRight = currentRight.next
            currentNode = currentNode.next

        return headNode.next
