'''
In this question one(1) is to be added to the array of digits, it had all carry and remainder,but i used an
easy approach
'''

def plusOne(self,digits):
    if len(digits)==0:
        digits = [1]
    elif digits[-1]==9:
        digits = self.digis[:-1]
        digits.extend([0])
    else:
        digits[-1] += 1
    return digits



'''
Another approach
'''

def plusOne(self,digits):
    n = len(digits)
    digits[n-1] += 1
    carry = digits[n-1]/10
    digits[n-1] = digits[n-1]%10

    for i in range(n-2,-1,-1):
        if carry ==1:
            digits[i]+=1
            carry = digits[i]/10
            digits[i] = digits[i]%10

    if carry==1:
        digits.insert(0,1)

    return digits