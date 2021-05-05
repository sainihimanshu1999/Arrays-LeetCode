def nextPermutation(self,nums):
    i=j=len(nums)-1

    while i>0 and nums[i-1]>=nums[i]:
        i-=1

    #if the list is in all reverse
    if i == 0:
        nums.reverse()
        return

    k = i-1
    #finding the last ascending postion
    while nums[j]<=nums[k]:
        j-=1

    nums[j],nums[k] = nums[k],nums[j]

    #reversing the second part
    left,right = k+1,len(nums)-1
    while left<right:
        nums[left],nums[right] = nums[right],nums[left]
        left += 1
        right -=1
