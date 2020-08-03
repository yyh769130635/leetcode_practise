# -*- coding: utf-8 -*-
# @Time : 7/30/2020 12:29 PM
# @Author : Peter yang


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        dummy = ListNode(-1)
        dummy.next = head
        pre = dummy

        while head and head.next:
            first = head
            second = head.next

            pre.next = second
            first.next = second.next
            second.next = first

            head = first.next
            pre = first
        return dummy.next
