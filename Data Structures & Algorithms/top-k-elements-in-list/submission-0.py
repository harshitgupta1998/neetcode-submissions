class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # c={}
        # for i in nums:
        #     c[i]=1+c.get(i,0)
        c=Counter(nums)
        #heap=heapq.heapify(c)
        print(c)
        heap=[]
        for i in c.keys():
            heapq.heappush(heap,(c[i],i))  
            if len(heap)>k:
                heapq.heappop(heap)
        res=[]
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res            