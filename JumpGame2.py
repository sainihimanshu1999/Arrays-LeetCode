'''
In thid question we take two variable, curr_cover and last_jump_index, curr_cover maintains the 
distance we travelled and last_jump_index maintains the current index we are on.
'''

def jumpGame(self,nums):
    n = len(nums)

    if n ==1:
        return 0

    destination = n-1
    curr_cover = 0
    last_jump_index = 0
    count = 0

    for i in range(n):
        curr_cover = max(curr_cover,i+nums[i])

        if  i == last_jump_index:
            last_jump_index = curr_cover
            count +=1
            if curr_cover>=destination:
                return count

    return count
