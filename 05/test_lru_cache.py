from unittest import TestCase

from lru_cache import LRUCache


class TestLruCache(TestCase):
    def test_lru_cache_2(self):
        cache = LRUCache(2)

        cache.set("k1", "val1")
        cache.set("k2", "val2")

        assert cache.get("k3") is None
        assert cache.get("k2") == "val2"
        assert cache.get("k1") == "val1"

        cache.set("k3", "val3")

        assert cache.get("k3") == "val3"
        assert cache.get("k2") is None
        assert cache.get("k1") == "val1"

        cache.set("k3", "new_val")
        cache.set("k4", "val4")

        assert cache.get("k1") is None
        assert cache.get("k3") == "new_val"
        assert cache.get("k4") == "val4"

    def test_lru_cache_1(self):
        cache = LRUCache(1)

        cache.set("k1", "val1")
        cache.set("k1", "val2")

        assert cache.get("k1") == "val2"

        cache.set("k2", "val2")

        assert cache.get("k1") is None
        assert cache.get("k2") == "val2"
