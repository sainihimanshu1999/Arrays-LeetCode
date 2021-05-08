def majorityElement(self, nums):
        dic = {}
        
        for num in nums:
            dic[num] = dic.get(num,0)+1
            
        for k,v in dic.items():
            if v >(len(nums)/2):
                return k


'''
New approach - Boyer Moore Majority Vote Algorithm
'''

def majorityElement(self,nums):
    candidate =0
    count = 0

    for n in nums:
        if n == candidate:
            count +=1

        elif count == 0:
            candidate = n
            count +=1

        else:
            count -=1

    return candidate
        