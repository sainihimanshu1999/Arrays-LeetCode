def rotate(self,nums,k):
    k = k%len(nums)

    nums[:k],nums[k:] = nums[len(nums)-k:],nums[:len(nums)-k]
