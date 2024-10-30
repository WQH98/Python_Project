class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        ret_list_head = ListNode()
        ret_cur = ret_list_head
        while (list1 is not None) and (list2 is not None):
            if list1.val <= list2.val:
                ret_new = ListNode(list1.val, None)
                list1 = list1.next
            else:
                ret_new = ListNode(list2.val, None)
                list2 = list2.next
            ret_cur.next = ret_new
            ret_cur = ret_new

        if list1 is not None:
            ret_cur.next = list1
        if list2 is not None:
            ret_cur.next = list2

        return ret_list_head.next


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
