def threeSum(self,nums):
    nums.sort()
    n = len(nums)
    answer = []

    #to remove dulpicates in 3sum
    for i in range(n):
        if i>0 and nums[i]==nums[i-1]:
            continue
        target = nums[i]*-1
        start,end = i+1,n-1

        #2sum formula
        while start<=end:
            if nums[start]+nums[end]==target:
                answer.append([nums[i],nums[start],nums[end]])
                #to remove dupliactes in 2sum
                while start<end and nums[start]==nums[start-1]:
                    start += 1
            elif nums[start]+nums[end]<target:
                start+= 1
            else:
                end -=1

    return answer
