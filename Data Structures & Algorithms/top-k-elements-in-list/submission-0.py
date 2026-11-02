from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        tracker = defaultdict(int)
        result = []

        for num in nums:
            tracker[num] += 1

        for j in range(k):
            most_frequent = max(tracker, key = tracker.get)
            result.append(most_frequent)
            del tracker[most_frequent]
        return result