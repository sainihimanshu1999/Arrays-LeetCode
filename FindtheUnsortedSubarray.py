'''
intialize two pointer start and end at the begining and move them when the element of sorted and unsorted
are equal, when they are stopped measure thier difference
'''

def findUnsorted(self,nums):
    sorted_nums = sorted(nums)
    start = 0
    end = len(nums)-1

    if sorted_nums == nums:
        return 0

    while sorted_nums[start] == nums[start]:
        start +=1

    while sorted_nums[end] == nums[end]:
        end -=1

    return end-start+1