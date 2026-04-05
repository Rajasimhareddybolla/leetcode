class Node:
    def __init__(self):
        self.vocab = {}
        self.isEnd = False
        self.word = ""
class Trie:
    def __init__(self):
        self.node = Node()
    def add(self , word):
        node = self.node
        for c in word:
            if c not in node.vocab:
                node.vocab[c] = Node()
            node = node.vocab[c]
        node.isEnd =True
        node.word = word
        return True


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie()
        m , n = len(board) , len(board[0])
        for word in words:
            trie.add(word)
        poss = [[0,1],[1,0],[-1,0],[0 ,-1]]
        res  = []
        def valid(i,j):
            if 0<=i<m and 0<=j<n:return True
            return False
        def search(i , j , t):
            if t.isEnd:
                res.append(t.word)
                t.isEnd = False
            c = board[i][j]
            if c not in t.vocab:
                return False
            board[i][j] = -1 
            for dx , dy in poss:
                x , y = i + dx , j+dy
                if valid(x, y):
                    search(x , y , t.vocab[c])
            board[i][j] = c
        for i in range(m):
            for j in range(n):
                search(i , j , trie.node)
        return res