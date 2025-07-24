# https://leetcode.com/problems/add-two-numbers/


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def to_list(node):
    res = []
    while node:
        res.append(node.val)
        node = node.next
    return res


def from_list(lst):
    head = ListNode(lst[0])
    current = head
    for val in lst[1:]:
        current.next = ListNode(val)
        current = current.next
    return head


# First approach - map linked list to array, then convert to int, then add, then convert back to linked list


class Solution:
    def addTwoNumbers(self, l1, l2):
        locally = False
        if not isinstance(l1, list):
            l1 = to_list(l1)
            locally = True
        if not isinstance(l2, list):
            l2 = to_list(l2)
            locally = True
        
        result = list(
            map(int, str(int("".join(map(str, l1[::-1]))) + int("".join(map(str, l2[::-1])))))
        )[::-1]
        
        return result if locally else from_list(result)    


# https://leetcode.com/problems/add-two-numbers/solutions/5184763/video-simple-addition-algorithm-python-javascript-java-and-c/


class Solution:
    def addTwoNumbers(self, l1, l2):
        locally = False

        if not isinstance(l1, ListNode):
            l1 = from_list(l1)
            locally = True
        if not isinstance(l2, ListNode):
            l2 = from_list(l2)
            locally = True

        dummy = ListNode()
        result = dummy

        total = carry = 0

        while l1 or l2 or carry:
            total = carry

            if l1:
                total += l1.val
                l1 = l1.next
            if l2:
                total += l2.val
                l2 = l2.next

            num = total % 10
            carry = total // 10
            dummy.next = ListNode(num)
            dummy = dummy.next

        return to_list(result.next) if locally else result.next
