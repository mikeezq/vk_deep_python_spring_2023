from unittest import TestCase

from lru_cache import LRUCache


class TestLruCache(TestCase):
    def setUp(self):
        self.cache = LRUCache(2)

    def test_lru_cache(self):
        self.cache.set("k1", "val1")
        self.cache.set("k2", "val2")

        assert self.cache.get("k2") == "val2"
        assert self.cache.get("k3") is None

        self.cache.set("k3", "val3")
        assert self.cache.get("k1") is None
        assert self.cache.get("k2") == "val2"
        assert self.cache.get("k3") == "val3"

        self.cache.set("k2", "new_val2")
        assert self.cache.get("k2") == "new_val2"

        self.cache.set("k4", "val4")
        assert self.cache.get("k4") == "val4"

        assert self.cache.get("k3") is None
