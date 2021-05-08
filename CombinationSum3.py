'''
This question was like the previous questions only, only difference was length of path is defined
'''

def CombinationSum3(self,n,k):
    nums = [1,2,3,4,5,6,7,8,9]
    result = []
    self.dfs(nums,0,n,[],result,k)
    return result

def dfs(self,nums,start,target,path,result,k):
    if target<0:
        return result

    if target == 0:
        if len(path)==k:
            result.append(path)
            return result

    for i in range(start,len(nums)):
        if nums[i]>target:
            break
        self.dfs(nums,i+1,target-nums[i],path +[nums[i]],result,k)
