"""
File: add2.py
Name: Jay Yin
------------------------
"""

import sys


class ListNode:
    def __init__(self, data=0, pointer=None):
        self.val = data
        self.next = pointer


def add_2_numbers(l1: ListNode, l2: ListNode) -> ListNode:
    #######################
    """
    Create a sequences of ListNodes 'l3',
    each ListNode contains the sum up value of the same order ListNode from l1 and l2.

    Then revise l3:
    Make sure each ListNode value is <10.
    If it's >=10, keep the units digit, and add one to the next ListNode's value.
    return the revised l3.
    """
    cur1 = l1
    cur2 = l2
    l3 = ListNode(cur1.val + cur2.val, None)
    cur3 = l3
    while True:
        if cur1.next is not None and cur2.next is not None:
            cur1 = cur1.next
            cur2 = cur2.next
            cur3.next = ListNode(cur1.val + cur2.val, None)
            cur3 = cur3.next
        elif cur1.next is None and cur2.next is not None:
            cur2 = cur2.next
            cur3.next = ListNode(cur2.val, None)
            cur3 = cur3.next
        elif cur1.next is not None and cur2.next is None:
            cur1 = cur1.next
            cur3.next = ListNode(cur1.val, None)
            cur3 = cur3.next
        else:
            cur = l3
            while cur.next is not None:
                if cur.val >= 10:
                    cur.val = cur.val % 10
                    cur.next.val = cur.next.val + 1
                cur = cur.next
            if cur.val >= 10:  # last data
                cur.val = cur.val % 10
                cur.next = ListNode(1, None)
            return l3

####### DO NOT EDIT CODE BELOW THIS LINE ########


def traversal(head):
    """
    :param head: ListNode, the first node to a linked list
    -------------------------------------------
    This function prints out the linked list starting with head
    """
    cur = head
    while cur.next is not None:
        print(cur.val, end='->')
        cur = cur.next
    print(cur.val)


def main():
    args = sys.argv[1:]
    if not args:
        print('Error: Please type"python3 add2.py test1"')
    else:
        if args[0] == 'test1':
            l1 = ListNode(2, None)
            l1.next = ListNode(4, None)
            l1.next.next = ListNode(3, None)
            l2 = ListNode(5, None)
            l2.next = ListNode(6, None)
            l2.next.next = ListNode(4, None)
            ans = add_2_numbers(l1, l2)
            print('---------test1---------')
            print('l1: ', end='')
            traversal(l1)
            print('l2: ', end='')
            traversal(l2)
            print('ans: ', end='')
            traversal(ans)
            print('-----------------------')
        elif args[0] == 'test2':
            l1 = ListNode(9, None)
            l1.next = ListNode(9, None)
            l1.next.next = ListNode(9, None)
            l1.next.next.next = ListNode(9, None)
            l1.next.next.next.next = ListNode(9, None)
            l1.next.next.next.next.next = ListNode(9, None)
            l1.next.next.next.next.next.next = ListNode(9, None)
            l2 = ListNode(9, None)
            l2.next = ListNode(9, None)
            l2.next.next = ListNode(9, None)
            l2.next.next.next = ListNode(9, None)
            ans = add_2_numbers(l1, l2)
            print('---------test2---------')
            print('l1: ', end='')
            traversal(l1)
            print('l2: ', end='')
            traversal(l2)
            print('ans: ', end='')
            traversal(ans)
            print('-----------------------')
        elif args[0] == 'test3':
            l1 = ListNode(0, None)
            l2 = ListNode(0, None)
            ans = add_2_numbers(l1, l2)
            print('---------test3---------')
            print('l1: ', end='')
            traversal(l1)
            print('l2: ', end='')
            traversal(l2)
            print('ans: ', end='')
            traversal(ans)
            print('-----------------------')
        else:
            print('Error: Please type"python3 add2.py test1"')


if __name__ == '__main__':
    main()
