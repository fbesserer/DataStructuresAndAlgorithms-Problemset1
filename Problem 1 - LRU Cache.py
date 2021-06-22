'''
Least Recently Used Cache

We have briefly discussed caching as part of a practice problem while studying hash maps.

The lookup operation (i.e., get()) and put() / set() is supposed to be fast for a cache memory.

While doing the get() operation, if the entry is found in the cache, it is known as a cache hit. If, however, the entry is not found, it is known as a cache miss.

When designing a cache, we also place an upper bound on the size of the cache. If the cache is full and we want to add a new entry to the cache, we use some criteria to remove an element. After removing an element, we use the put() operation to insert the new element. The remove operation should also be fast.

For our first problem, the goal will be to design a data structure known as a Least Recently Used (LRU) cache. An LRU cache is a type of cache in which we remove the least recently used entry when the cache memory reaches its limit. For the current problem, consider both get and set operations as an use operation.

Your job is to use an appropriate data structure(s) to implement the cache.

    In case of a cache hit, your get() operation should return the appropriate value.
    In case of a cache miss, your get() should return -1.
    While putting an element in the cache, your put() / set() operation must insert the element. If the cache is full, you must write code that removes the least recently used entry first and then insert the element.

All operations must take O(1) time.
'''
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_node(self, value):
        new_node = Node(value)
        head = self.head
        if not head:
            self.head = new_node
            self.tail = self.head
        else:  # add to the front of the list
            new_node.next = head
            head.prev = new_node
            self.head = new_node
        return new_node

    def pop(self):
        # called from LRU_Cache once the cache is full in order to remove the least used item
        if self.head == self.tail:  # if cache size = 1
            key = self.tail.value
            self.head, self.tail = None, None
            return key
        key = self.tail.value
        self.tail = self.tail.prev
        self.tail.next = None
        return key

    def place_front(self, node):
        if self.head == node:  # node is already head of dll
            return
        elif self.tail == node:  # node is at the end of dll
            self.tail = node.prev
            node.prev.next = None
            node.prev = None
            node.next = self.head
            self.head.prev = node
            self.head = node
            return
        else:
            # ensure that the two adjacent nodes point to each other
            node.prev.next = node.next
            node.next.prev = node.prev
            node.prev = None
            node.next = self.head
            self.head.prev = node
            self.head = node


class CacheSizeError(Exception):
    pass


class LRU_Cache(object):

    def __init__(self, capacity):
        self.capacity = abs(capacity)
        self.table = dict()
        self.dll = DoublyLinkedList()

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent.
        # bring node to the front
        if key in self.table:
            node = self.table[key][0]
            value = self.table[key][1]
            self.dll.place_front(node)
            return value
        return -1

    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item.
        if self.capacity == 0:
            raise CacheSizeError("current cache size: 0. Set a cache size > 0 when initializing a LRU_Cache object.")
        if len(self.table.keys()) < self.capacity:
            if key in self.table:
                # put node to front of list
                node = self.table[key][0]
                self.dll.place_front(node)
                return
            # add new key, value pair
            self.table[key] = (self.dll.add_node(key), value)
        else:
            self.delete()
            self.table[key] = (self.dll.add_node(key), value)

    def delete(self):
        key = self.dll.pop()
        del self.table[key]


# Testcases

print("-------Testcase Nr. 1 --------")
our_cache = LRU_Cache(5)

our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(3, 3)
print(our_cache.get(3))  # returns 3
print(our_cache.get(1))  # returns 1

our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(3, 3)
our_cache.set(4, 4)

print(our_cache.get(1))      # returns 1
print(our_cache.get(2))       # returns 2
print(our_cache.get(9))      # returns -1 because 9 is not present in the cache

our_cache.set(5, 5)
our_cache.set(6, 6)
print(our_cache.get(3))      # returns -1 because the cache reached it's capacity and 3 was the least recently used entry

print("-------Testcase Nr. 2 --------")
cache = LRU_Cache(1)

cache.set(1, 1)
cache.set(2, 2)
print(cache.get(1))  # returns -1
print(cache.get(2))  # returns 2

print("-------Testcase Nr. 3 --------")

cache = LRU_Cache(5)

cache.set(1, 1)
cache.set(1, 1)
cache.set(1, 1)
cache.set(1, 1)
cache.set(2, 2)
cache.set(3, 3)
cache.set(4, 4)
cache.set(5, 5)

print(cache.get(1))  # returns 1
print(cache.get(2))  # returns 2
print(cache.get(3))  # returns 3
print(cache.get(4))  # returns 4
print(cache.get(5))  # returns 5


print("-------Testcase Nr. 4 --------")

cache = LRU_Cache(0)

cache.set(1, 1)  # raises CachSizeError