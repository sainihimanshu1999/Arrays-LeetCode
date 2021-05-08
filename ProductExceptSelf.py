'''
In this question output array is created, output[i] is moved forward, and then backward
'''

def product(self,nums):
    output = []
    p = 1
    n = len(nums)

    for i in range(n):
        output.append(p)
        p = p *nums[i]


    for i in range(n)[::-1]:
        output[i] = output[i]*p
        p = p *nums[i]

    return output