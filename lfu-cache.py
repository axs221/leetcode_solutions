# https://leetcode.com/problems/lfu-cache/

from time import time

class LFUCache(object):

    def __init__(self, capacity):
        self.capacity = capacity
        self.usage_id = 0
        self.keys = dict()

    def get(self, key):
        value = [-1,0,0]
        if key in self.keys:
            value = self.keys[key]
        value[1] = value[1] + 1
        value[2] = self.usage_id
        self.usage_id += 1
        return value[0]

    def least_used_or_oldest(self, value1, value2):
        if value1[1][1] < value2[1][1]:
            return value1
        elif value1[1][1] > value2[1][1]:
            return value2
        else:
            return value1 if value1[1][2] < value2[1][2] else value2

    def __evict_LFU(self):
        LFU = reduce(self.least_used_or_oldest, self.keys.iteritems())
        if LFU:
            del self.keys[LFU[0]]

    def set(self, key, value):
        if self.capacity <= 0:
            return

        item = self.keys.get(key)

        usage_id = 0
        # if len(item) > 0:
        if item:
            if value != item[0]:
                self.usage_id += 1
                usage_id = self.usage_id
            else:
                usage_id = item[2]
        else:
            self.usage_id += 1
            usage_id = self.usage_id

            if len(self.keys) >= self.capacity:
                self.__evict_LFU()

        usage_count = 1 if not item else item[1] + 1

        if not item:
            self.keys[key] = [value, usage_count, usage_id]
        else:
            item[0] = value
            item[1] = usage_count
            item[2] = usage_id


