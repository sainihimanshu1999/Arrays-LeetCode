'''
Simple way to code up the answer, but i think the time complexity must be higher
'''

def search(self,nums,target):
    if target in nums:
        return nums.index(target)
    else:
        return -1



'''
Using binary search to code up the answer, the time complexity must be less in this
'''

def binarysearch(self,nums,target):
    if not nums:
        return -1

    low,high = 0,len(nums)-1

    while low<=high:
        mid = (low+high)//2
        if nums[mid] == target:
            return mid
        #the extra layer of protection is because it is pivoted to either side
        if nums[low]<=nums[mid]:
            if nums[low]<=target<=nums[mid]:
                high = mid-1
            else:
                low = mid+1
        else:
            if nums[mid]<=target<=nums[mid]:
                low = mid+1
            else:
                high = mid-1

    return -1