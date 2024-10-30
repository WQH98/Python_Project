class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        # 终止条件 直到两个链表都为空
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        if list1.val <= list2.val:  # 递归调用
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2


if __name__ == "__main__":
    l1_arr = [1, 2, 4]
    l2_arr = [1, 3, 4]
    l1_head = ListNode()
    l1_cur = l1_head
    for i in range(0, len(l1_arr)):
        l1_new = ListNode(l1_arr[i], None)
        l1_cur.next = l1_new
        l1_cur = l1_new
    l2_head = ListNode()
    l2_cur = l2_head
    for i in range(0, len(l2_arr)):
        l2_new = ListNode(l2_arr[i], None)
        l2_cur.next = l2_new
        l2_cur = l2_new
    solution = Solution()
    ret_head = solution.mergeTwoLists(l1_head.next, l2_head.next)
    while ret_head is not None:
        print(ret_head.val)
        ret_head = ret_head.next
