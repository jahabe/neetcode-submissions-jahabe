class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        left, right = head, head

        # right를 n칸 앞으로
        for i in range(n):
            right = right.next

        # head 자체를 삭제해야 하는 경우
        if right is None:
            return head.next

        # 둘이 같이 이동
        while right.next:
            left = left.next
            right = right.next

        left.next = left.next.next
        return head