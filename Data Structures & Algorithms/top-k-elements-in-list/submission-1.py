class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {} 
        for num in nums: 
            count[num] = 1 + count.get(num, 0)

        # empty min heap
        heap = []

        # for each number in frequnecy amap
        for num in count.keys():
            # push (frequency, number) into the heap
            heapq.heappush(heap, (count[num], num))
            # if the heap size becomes greater than k,  
            if len(heap) > k: 
                # pop once to remove the smallest frequency.
                heapq.heappop(heap)
        
        res = []
        for i in range(k): 
            res.append(heapq.heappop(heap)[1])
        return res