'''
In this question we are given a flower bed and we have to keep in mind that, if x is the consecutive empty
spots, number of flowers that can be planted is x-1//2.
'''

def flowerCount(self,flowerbed,n):
    count = 1
    numberofFlower = 0

    for i in flowerbed:
        if i == 1:
            numberofFlower += (count-1)//2
            count = 0

        else:
            count += 1

    if count>1:
        numberofFlower += count//2

    return numberofFlower>=n