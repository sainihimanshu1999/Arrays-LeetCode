'''
Binary search id used in this, moreoever if we sort any array we can use binary search in that
'''

def search(self,nums,target):
    if not nums:
        return False

    nums.sort()

    low,high = 0,len(nums)-1

    while low<=high:
        mid = (low+high)//2

        if nums[mid]==target:
            return True

        elif num[mid]<target:
            low = mid+1
        else:
            high = mid-1
    return False