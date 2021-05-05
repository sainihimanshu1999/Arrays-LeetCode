'''
First intution code
'''

def searchRange(self,nums,target):
    if target not in nums:
        return [-1,-1]
    op = []
    for i in range(len(nums)):
        if nums[i]==target:
            op.append(i)
            break

    for i in range(len(nums))[::-1]:
        if nums[i]== target:
            op.append(i)
            break

    return op


'''
Using Binary Search, it is very fast
'''

def searchRange(self,nums,target):
    low , high = 0, len(nums)-1

    first = self. firstIndex(self,nums,low,high,target)
    last = self.lastIndex(self,nums,low,high,target)

    return [first,last]

def firstIndex(self,nums,low,high,target):
    res = -1
    while low<=high:
        mid = (low+high)//2
        if nums[mid]==target:
            res = mid
            high = mid-1
        elif nums[mid]>target:
            high = mid-1
        else:
            low = mid+1

    return res

def lastIndex(self, nums, low, high, target):
    res = -1
    while low<=high:
        mid = (low+high)//2
        if nums[mid] == target:
            res = mid
            low = mid+1
        
        elif nums[mid]>target:
            high = mid-1

        else:
            low = mid+1

    return res