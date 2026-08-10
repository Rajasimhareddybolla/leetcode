class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.isLeaf = False



class PrefixTree:


    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root

        for i in range(len(word)):
            c = word[i]
            i = ord(c) - ord('a')
            if curr.children[i] == None:
                curr.children[i] = TrieNode()
            
            curr = curr.children[i]
        curr.isLeaf = True

    def search(self, word: str) -> bool:
        curr = self.root

        for i in range(len(word)):
            c = word[i]
            i = ord(c) - ord('a')
            if curr.children[i] == None:
                return False
            curr = curr.children[i]
        return curr.isLeaf

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        word = prefix
        for i in range(len(word)):
            c = word[i]
            i = ord(c) - ord('a')
            if curr.children[i] == None:
                return False
            curr = curr.children[i]
        return True