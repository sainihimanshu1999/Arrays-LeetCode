def CombinationSum(self,candidates,target):
    result = []
    self.dfs(candidates,target,[],result)
    return result

def dfs(self,nums,target,path,result):
    if target<0:
        return result

    if target == 0:
        result.append(path)
        return result

    for i in range(len(nums)):
        self.dfs(nums[i:],target-nums[i],path+[nums[i]],result)