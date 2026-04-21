class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # 1단계: 중간 찾기
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # slow가 중간 → 두번째 절반 시작
        second = slow.next
        slow.next = None   # 첫번째 절반 끊기

        # 2단계: 두번째 절반 reverse
        prev = None
        curr = second
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        second = prev  # reverse된 리스트의 head

        # 3단계: 두 리스트 합치기
        first = head
        while second:
            next_first = first.next
            next_second = second.next
            first.next = second
            second.next = next_first
            first = next_first
            second = next_second