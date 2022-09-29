class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        heap = []
        result = []
        for i in arr:
            heapq.heappush(heap, (abs(i - x), i))
        
        while k > 0:
            result.append(heapq.heappop(heap)[1])
            k-= 1
        
        return sorted(result)