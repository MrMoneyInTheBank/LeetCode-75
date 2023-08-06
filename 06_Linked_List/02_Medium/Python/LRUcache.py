class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev, self.next = None, None


class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.cap = capacity

        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left

    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    def insert(self, node):
        prev, right = self.right.prev, self.right
        prev.next = right.prev = node
        node.next = right
        node.prev = prev

    def update(self, node):
        self.remove(node)
        self.insert(node)

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self.update(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        node = Node(key, value)
        self.cache[key] = node
        self.insert(node)

        if len(self.cache) > self.cap:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]


# Time | Space : O(1) | O(n)

# At each point, we need to keep track of the last and most recent added key. A double linked list allows
# Us to keep track of the head and tail of the list in constant time and that is why this data structure is used
# instead of a 2-D array. To use a doublly linked list, we first create a Node class. Each node will hold the key
# and value of a query. In addition to this, each node will also have a pointer to the next and previous node which
# will be None by default. In our LRU cache class, we first initialize self.cap = capacity to keep track of the maximum
# cache size. Next, our actual cache will be a dictionary which maps the key of the query to the node that it corresponds
# to in the doubly linked list. For the get method, if the given key is not in the cache, it is not in the list and therefore
# we can return -1. If it is in the cache, then the value associated with it will be stored in the Node.val attribute. After
# we get the node, we must update its position by first removing it from wherever it is located and adding it all the way
# on the right (except the tail which we use to get the most recent key). For the put method, if the given key is already
# in the cache, we need to update the value and reposition it. We can simply remove it, and then insert it again. In our cache
# we now store this node mapped to the given key. Now we check the length of the cache and if it is greater than self.cap, we
# need to remove the least recently used key. We can do this by removing the leftmost node.
