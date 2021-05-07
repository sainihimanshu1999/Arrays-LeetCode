'''
In this question we have to remove duplicate form the sorted array. Two pointer approach comes in handy,
we will intialize two pointer, one slow and one fast then keep it on the number of duplicate numbers we
have to remove, in this case it is two. If nums[slow-k]==nums[k] then there more equal number of numbers
are present so we don't move the slow pointer and in any case just move the fast pointer.
'''

def removeDuplicates(self,nums):
    if len(nums)<2:
        return len(nums)

    slow,fast = 2,2

    while fast<len(nums):
        if nums[slow-2]!=nums[fast]:
            nums[slow]=nums[fast]
            slow+=1
        fast +=1

    return slow