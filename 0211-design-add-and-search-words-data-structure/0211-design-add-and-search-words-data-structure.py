class WordDictionary:

    def __init__(self):
        self.root = {}

    def addWord(self, word: str) -> None:
        node = self.root
        for c in word:
            if c not in node:
                node[c] = {}
            node = node[c]
        node["*"] = True

    def search(self, word: str) -> bool:
        def dfs(node,i):
            if i == len(word):
                return "*" in node
            
            c = word[i]

            if c == ".":
                for letter in node:
                    if letter != "*" and dfs(node[letter], i+1):
                        return True
                return False
            
            if c not in node:
                return False

            return dfs(node[c], i+1)
        
        return dfs(self.root, 0)
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)