"""
Problem - https://leetcode.com/problems/lru-cache/description/
"""

class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.lru_cache = {}
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def delete_node(self, node):
        """
        :type node: Node
        :rtype: None
        """
        node.prev.next = node.next
        node.next.prev = node.prev

    def add_node(self, node):
        """
        :type node: Node
        :rtype: None
        """
        temp_node = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next = temp_node
        temp_node.prev = node

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.lru_cache:
            return -1

        mru_node = self.lru_cache.get(key)

        self.delete_node(mru_node)
        self.add_node(mru_node)

        return mru_node.val

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        new_node = Node(key, value)

        if key in self.lru_cache:
            key_node = self.lru_cache.get(key)
            key_node.val = value
            self.delete_node(key_node)
            self.add_node(key_node)
            return 

        if len(self.lru_cache) < self.capacity:
            self.add_node(new_node)
        else:
            lru_node = self.tail.prev
            self.delete_node(lru_node)
            self.add_node(new_node)
            self.lru_cache.pop(lru_node.key)

        self.lru_cache[key] = new_node



# Your LRUCache object will be instantiated and called as such:
obj = LRUCache(1)
obj.put(2,1)
# obj.put(2,2)
print(obj.get(2))
# obj.put(3,3)
# print(obj.get(2))
# obj.put(4,4)
# print(obj.get(1))
# print(obj.get(3))
# print(obj.get(4))
print(obj.lru_cache)