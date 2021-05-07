def majorityElement(self, nums):
        dic = {}
        
        for num in nums:
            dic[num] = dic.get(num,0)+1
            
        for k,v in dic.items():
            if v >(len(nums)/2):
                return k
        