'''
This is a universal way of finding the subset
'''

def subsets(self,nums):
    if not nums:
        return []

    x = [[]]

    for i in range(len(nums)):
        for j in range(len(x)):
            x.append(x[j]+[nums[i]])


    return x



'''
another way of solving
'''

def subset(self,nums):
    result = []
    self.dfs(sorted(nums),[],result)
    return result

def dfs(self,nums,path,result):
    result.append(path)

    for i in range(len(nums)):
        self.dfs(nums[i+1:],path+[nums[i]],result)