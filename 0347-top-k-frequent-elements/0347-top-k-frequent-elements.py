class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        #Initialiaze bucket as a list of empty lists
        bucket = [[] for _ in range(len(nums) + 1)]
        frequencyMap = {}
        
        #fill frequencymap
        for n in nums:
            if n not in frequencyMap:
                frequencyMap[n] = 1
            else:
                frequencyMap[n] += 1
        
        #fill bucket 
        for key,frequency in frequencyMap.items():
            bucket[frequency].append(key)
        result = []
        
        #iterate bucket in reverse to get top k freq elements
        for i in reversed(range(len(bucket))):
            if bucket[i]:
                for value in bucket[i]:
                    if len(result)<k:
                        result.append(value)
                    else:
                        return result
        return result
