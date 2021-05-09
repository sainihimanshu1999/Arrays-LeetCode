'''
Using three sliding windows
'''
def maxSumOfThreeSubArrays(self,nums,k):
    bestSeq = 0
    bestTwoSeq = [0,k]
    bestThreeSeq = [0,k,k*2]

    seqSum = sum(nums[0:k])
    seqTwoSum = sum(nums[k:k*2])
    seqThreeSum = sum(nums[k*2:k*3])

    bestSeqSum = seqSum
    bestTwoSum = seqSum+seqTwoSum
    bestThreeSum = seqSum + seqTwoSum + seqThreeSum

    seqIndex = 1
    twoSeqIndex = k+1
    threeSeqIndex = k*2+1

    while threeSeqIndex<=len(nums)-k:
        seqSum = seqSum - nums[seqIndex-1]+nums[seqIndex+k-1]
        seqTwoSum = seqTwoSum - nums[twoSeqIndex-1] + nums[twoSeqIndex+k-1]
        seqThreeSum = seqThreeSum - nums[threeSeqIndex-1] + nums[threeSeqIndex+k-1]

        if seqSum>bestSeqSum:
            bestSeqSum = seqSum
            bestSeq = seqIndex

        if seqTwoSum + bestSeqSum > bestTwoSum:
            bestTwoSeq = [bestSeq,twoSeqIndex]
            bestTwoSum = seqTwoSum+bestSeqSum

        if seqThreeSum +bestTwoSum>bestThreeSum:
            bestThreeSum = seqThreeSum+bestTwoSum
            bestThreeSeq = bestTwoSeq+[threeSeqIndex]

        seqIndex +=1
        twoSeqIndex +=1
        threeSeqIndex +=1

    return bestThreeSeq