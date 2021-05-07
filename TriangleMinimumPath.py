'''
This question is bit tricky but can be solved by basic tabulation method
'''
def minimumPathofTriangle(self,triangle):
    op = [0]*(len(triangle)+1)

    for row in triangle[::-1]:
        for i in range(len(row)):
            op[i] = row[i]+min(op[i],op[i+1])

    return op[0]