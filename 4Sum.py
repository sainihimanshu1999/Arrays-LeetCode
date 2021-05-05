def fourSum(self,nums,target):
    dic = {}
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            sumi = nums[i]+nums[j]

            if sumi in dic:
                dic[sumi].append((i,j))

            else:
                dic[sumi] = [(i,j)]


    result = set()
    for key in dic:
        value = target-key
        if value in dic:
            list1 = dic[key]
            list2 = dic[value]

            for (i,j) in list1:
                for (k,l) in list2:
                    if i!=k and i!=l and j!=k and j!=l:
                        final = [nums[i],nums[j],nums[k],nums[l]]
                        final.sort()
                        result.add(tuple(final))
    return list(result)