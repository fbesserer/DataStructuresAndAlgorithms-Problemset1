'''
Union and Intersection of Two Linked Lists

Your task for this problem is to fill out the union and intersection functions. The union of two sets A and B is the set
of elements which are in A, in B, or in both A and B. The intersection of two sets A and B, denoted by A ∩ B, is the set
of all objects that are members of both the sets A and B.

You will take in two linked lists and return a linked list that is composed of either the union or intersection, respectively.
Once you have completed the problem you will create your own test cases and perform your own run time analysis on the code.
'''

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string

    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            self.tail = self.head
            return
        node = Node(value)
        self.tail.next = node
        self.tail = node

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size


def travers_union(ull, head, unique_vals):
    while head:
        if head.value not in unique_vals:
            ull.append(head.value)
            unique_vals.add(head.value)
        head = head.next


def union(llist_1, llist_2):
    """ returns union of two sets in form of a linkedlist """
    ull = LinkedList()
    unique_vals = set()
    # travers 1st linkedlist
    head = llist_1.head
    travers_union(ull, head, unique_vals)
    # travers 2nd linkedlist
    head = llist_2.head
    travers_union(ull, head, unique_vals)
    return ull


def intersection(llist_1, llist_2):
    """ returns intersection of two sets in form of a linkedlist """
    ill = LinkedList()
    unique_vals = set()

    head = llist_1.head
    while head:
        unique_vals.add(head.value)
        head = head.next

    head = llist_2.head
    while head:
        if head.value in unique_vals:
            ill.append(head.value)
            unique_vals.discard(head.value)
        head = head.next

    return ill


# Test case 1
print("----- Testcase Nr 1 -----")

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,21]
element_2 = [6,32,4,9,6,1,11,21,1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print (union(linked_list_1,linked_list_2))  # prints 3 -> 2 -> 4 -> 35 -> 6 -> 65 -> 21 -> 32 -> 9 -> 1 -> 11 ->
print (intersection(linked_list_1,linked_list_2))  # prints 6 -> 4 -> 21 ->

# Test case 2
print("----- Testcase Nr 2 -----")

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,23]
element_2 = [1,7,8,9,11,21,1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print (union(linked_list_3,linked_list_4))  # prints 3 -> 2 -> 4 -> 35 -> 6 -> 65 -> 23 -> 1 -> 7 -> 8 -> 9 -> 11 -> 21 ->
print (intersection(linked_list_3,linked_list_4))  # prints out nothing

# Test case 3
print("----- Testcase Nr 3 -----")

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = []
element_2 = []

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print (union(linked_list_3,linked_list_4))  # prints out nothing
print (intersection(linked_list_3,linked_list_4))  # prints out nothing