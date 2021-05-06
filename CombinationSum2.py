'''
It is different from combination sum 1 as in the previous one as, in revious one we can use numbers
from the list n time, here there is no duplicates allowed
'''

def CombinationSum2(self,candidates,target):
    candidates.sort()
    result = []
    self.dfs(candidates,0,target,[],result)
    return result

def dfs(self,nums,start,target,path,result):
    if target<0:
        return result
    
    if target == 0:
        result.append(path)
        return result

    for i in range(start,len(nums)):
        if i>start and nums[i]==nums[i-1]:
            continue

        if nums[i]>target:
            break

        self.dfs(nums,i+1,target-nums[i],path+[nums[i]],result)