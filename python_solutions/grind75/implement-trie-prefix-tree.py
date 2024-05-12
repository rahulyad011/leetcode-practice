# https://leetcode.com/problems/implement-trie-prefix-tree/

class TrieNode():
    def __init__(self) -> None:
        self.children = [None]*26
        self.end = False

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        currnode = self.root
        for c in word:
            ind = ord(c)-ord('a')
            if not currnode.children[ind]:
                currnode.children[ind] = TrieNode()
            currnode = currnode.children[ind]
        currnode.end = True

    def search(self, word: str) -> bool:
        currnode = self.root
        for c in word:
            ind = ord(c)-ord('a')
            if not currnode.children[ind]:
                return False
            currnode = currnode.children[ind]
        if currnode.end:
            return True

    def startsWith(self, prefix: str) -> bool:
        currnode = self.root
        for c in prefix:
            ind = ord(c)-ord('a')
            if not currnode.children[ind]:
                return False
            currnode = currnode.children[ind]
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)