class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:

        result = 0

        jobs = [(beg, end, profit) for beg, end, profit in zip(startTime, endTime, profit)]
        jobs.sort()
        
        heap = []        
        curr_profit = 0
        
        for beg, end, p in jobs:
            while heap and heap[0][0] <= beg:
                _, prev_profit = heapq.heappop(heap)
                curr_profit = max(curr_profit, prev_profit)
            
            heapq.heappush(heap, (end, curr_profit + p))
            
            result = max(result, curr_profit + p)

        return result