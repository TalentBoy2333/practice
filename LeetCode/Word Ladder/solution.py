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
        h = [0 for _ in range(len(wordList))]
        curWord = beginWord
        self.res = 0
        self.bfs(curWord, endWord, wordList, h, 0)
        return self.res

    def bfs(self, curWord, endWord, wordList, h, cur):
        for i in range(len(h)):
            if h[i] == 0:
                h[i] = 1
                if self.judge(curWord, wordList[i]):
                    if wordList[i] == endWord:
                        # print(wordList[i])
                        if self.res == 0:
                            self.res = cur + 1
                        elif self.res > cur + 1:
                            self.res = cur + 1
                    else:
                        # print(wordList[i])
                        self.bfs(wordList[i], endWord, wordList, h, cur+1)

        
    def judge(self, w1, w2):
        diff = 0
        for i in range(len(w1)):
            if w1[i] != w2[i]:
                diff += 1
        if diff <= 1:
            return True 
        else:
            return False

if __name__ == '__main__':
    beginWord = 'a'
    endWord = 'c'
    wordList = ["a","b","c"]
    so = Solution()
    res = so.ladderLength(beginWord, endWord, wordList)
    print(res)