import argparse
from logger import get_logger, add_stream_handler, add_filter


log = get_logger()


class Node:
    def __init__(self, key, value):
        log.debug("Creating new node, %s", self)
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
            log.info("Key %s in cache", key)
            node = self.cache[key]
            self._move_to_front(node)
            return node.value
        log.warning("Key %s not in cache", key)
        return None

    def set(self, key, value):
        if key in self.cache:
            log.info("Changing value for existing key %s to %s", key, value)
            node = self.cache[key]
            node.value = value
            self._move_to_front(node)
        else:
            log.info("Set new key %s, with value %s", key, value)
            node = Node(key, value)
            self.cache[key] = node
            self._add_to_front(node)

            if len(self.cache) > self.limit:
                self._remove_last()

    def _move_to_front(self, node):
        if node != self.head:
            log.debug("Node %s not head, move to front", node)
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
        log.debug("Add new node to front %s", node)
        if self.head:
            node.next = self.head
            self.head.prev = node
            self.head = node
        else:
            self.head = node
            self.tail = node

    def _remove_last(self):
        log.info("Removing cache tail, %s", self.tail.key)
        del self.cache[self.tail.key]
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None


def parse_args():
    args_parser = argparse.ArgumentParser()
    args_parser.add_argument("-s", action="store_true", help="log in stdout")
    args_parser.add_argument("-f", action="store_true", help="use custom filter")

    return args_parser.parse_args()


if __name__ == "__main__":
    args = parse_args()

    if args.s:
        log = add_stream_handler(log)

    if args.f:
        log = add_filter(log)

    cache = LRUCache(2)

    cache.set("k1", "val1")
    cache.set("k2", "val2")
    assert cache.get("k3") is None
    assert cache.get("k2") == "val2"
    assert cache.get("k1") == "val1"
    cache.set("new_key", "new_value")
    cache.set("new_key", "new_val")
