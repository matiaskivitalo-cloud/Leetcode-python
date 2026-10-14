# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
       self.val = val       
       self.next = next

class Solution:
    def mergeTwoLists(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
        dummy = ListNode()
        tail = dummy
        list_x = list1
        list_y = list2
        while list_x and list_y:
            if list_x.val <= list_y.val:
                tail.next = list_x
                list_x = list_x.next
            else:
                tail.next = list_y
                list_y = list_y.next
            tail = tail.next
        
        tail.next = list_x if list_x else list_y

        return dummy.next