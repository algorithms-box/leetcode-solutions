from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumber(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode(val=0)
        n1 = 0
        n2 = 0
        carry = 0
        current = head

        while l1 is not None or l2 is not None or carry != 0:
            if l1 is not None:
                n1 = l1.val
                l1 = l1.next
            else:
                n1 = 0

            if l2 is not None:
                n2 = l2.val
                l2 = l2.next
            else:
                n2 = 0

            current.next = ListNode(val=(n1+n2+carry) % 10)
            current = current.next
            carry = (n1+n2+carry)//10

        return head.next


def main():
    l11 = ListNode(val=8)
    l12 = ListNode(val=3, next=l11)
    l13 = ListNode(val=6, next=l12)

    l21 = ListNode(val=7)
    l22 = ListNode(val=1, next=l21)
    l23 = ListNode(val=9, next=l22)

    s = Solution()
    result = s.addTwoNumber(l13, l23)
    print(result.val)
    p = result.next
    while p is not None:
        print(p.val)
        if p.next is None:
            break
        else:
            p = p.next


if __name__ == "__main__":
    main()
