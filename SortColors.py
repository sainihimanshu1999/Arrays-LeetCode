'''
One appraoch is swapping numbers
'''

def sortcolors(self,nums):
    red,white,blue = 0,0,len(nums)-1

    while white<=blue:
        if nums[white]==0:
            nums[red],nums[white] = nums[white],nums[red]

        elif num[white]==1:
            white +=1

        else:
            nums[blue],nums[white] = nums[white],nums[blue]
            blue -=1


'''
another approach just sort numbers
'''

def sortcolors(self,nums):
    nums.sort()