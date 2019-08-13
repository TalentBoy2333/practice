from collections import defaultdict
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        if endWord not in wordList:
            return 0
        length = len(beginWord)
        d = self.judge(beginWord, wordList)
        q = [(beginWord, 1)]
        visited = []
        while q != []:
            # print(q)
            curWord, level = q.pop(0)
            for i in range(length):
                temp = curWord[:i] + '*' + curWord[i+1:]
                for w in d[temp]:
                    if w == endWord:
                        return level + 1
                    if w not in visited:
                        visited.append(w)
                        q.append((w, level+1))
                d[temp] = []
        return 0
        
    def judge(self, beginWord, wordList):
        d = defaultdict(list)
        l = [beginWord] + wordList
        length = len(beginWord)
        for word in l:
            for i in range(length):
                temp = word[:i] + '*' + word[i+1:]
                d[temp].append(word)
        return d


# if __name__ == '__main__':
#     beginWord = 'hit'
#     endWord = 'cog'
#     wordList = ["hot","dot","dog","lot","log","cog"]
#     # beginWord = "hot"
#     # endWord = "dog"
#     # wordList = ["hot","dog","cog","pot","dot"]
#     so = Solution()
#     res = so.ladderLength(beginWord, endWord, wordList)
#     print(res)