'''
In finding the duplicate generally dictionary works perfectly
'''

def findDuplicates(self, nums):
        result = []
        dic = {}
        for num in nums:
            dic[num] = dic.get(num,0)+1
            
        for k,v in dic.items():
            if v==2:
                result.append(k)
                
        return result