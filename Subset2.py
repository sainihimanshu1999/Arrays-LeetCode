'''
In this question duplicate numbers are there
'''

def subset2(self,nums):
    result = []
    self.dfs(sorted(subsets),[],result)
    return result

def dfs(self,nums,path,result):
    result.append(path)

    for i in range(len(nums)):
        if i>0 and nums[i-1]==nums[i]:
            continue

        self.dfs(nums[i+1:],path+[nums[i]],result)



'''
other way of solving
'''

def subset2(self, nums):
    x =[[]]
    nums.sort()
    for i in range(len(nums)):
        if  i == 0   or nums[i]!=nums[i-1]:
            l = len(x)

        for j in range(len(x)-l,len(x)):
            x.append(x[j]+[nums[i]])

    return x