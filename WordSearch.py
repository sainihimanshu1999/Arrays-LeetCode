'''
In this question, word is being sliced from beginning and then passed on to the function of dfs
'''

def exist(self,board,word):
    if not board:
        return False


    for i in range(len(board)):
        for j in range(len(board[0])):
            if self.dfs(board,i,j,word):
                return True

    return False


def dfs(self,board,i,j,word):
    if len(word) == 0:
        return True

    if i<0 or i>=len(board) or j<0 por j>=len(board[0]) or word!= board[i][j]:
        return False

    char = board[i][j]
    board[i][j] = '#'

    res = self.dfs(board,i+1,j,word[1:]) or self.dfs(board,i-1,j,word[1:]) or self.dfs(board,i,j+1,word[1:]) or self.dfs(board,i,j-1,word[i:])
    board[i][j] = char
    return res