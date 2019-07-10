# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 18:29:53 2019

@author: user
"""
#21. Merge Two Sorted Lists

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        curr=dummy=ListNode(0)  #虛擬的起始點
        
        while l1 and l2:
            if l1.val < l2.val:
                curr.next=l1
                l1=l1.next
            else:
                curr.next=l2
                l2=l2.next
            curr=curr.next
        curr.next=l1 or l2  #最後結束的也要插入
        
        return dummy.next