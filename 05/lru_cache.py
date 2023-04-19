class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, limit=42):
        self.limit = limit
        self.cache = {}
        self.head = None
        self.tail = None

    def get(self, key):
        if key in self.cache:
            node = self.cache[key]
            self._move_to_front(node)
            return node.value
        return None

    def set(self, key, value):
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self._move_to_front(node)
        else:
            node = Node(key, value)
            self.cache[key] = node
            self._add_to_front(node)

            if len(self.cache) > self.limit:
                self._remove_last()

    def _move_to_front(self, node):
        if node != self.head:
            if node.prev:
                node.prev.next = node.next
            if node.next:
                node.next.prev = node.prev
            if node == self.tail:
                self.tail = node.prev

            node.prev = None
            node.next = self.head
            self.head.prev = node
            self.head = node

    def _add_to_front(self, node):
        if self.head:
            node.next = self.head
            self.head.prev = node
            self.head = node
        else:
            self.head = node
            self.tail = node

    def _remove_last(self):
        del self.cache[self.tail.key]
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
