class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        res = self.dfs(s, wordDict, {})
        # print(res)
        return res

    def dfs(self, s, wordDict, map):
        if s in map:
            return map[s]
        res = []
        if s == '':
            res.append('')
            return res
        for word in wordDict:
            if s.startswith(word):
                sublist = self.dfs(s[len(word):], wordDict, map)
                for sub in sublist:
                    if sub == '':
                        res.append(word + '' + sub)
                    else:
                        res.append(word + ' ' + sub)

        map[s] = res
        return res           


# string = "catsanddog"
# wordDict = ["cat", "cats", "and", "sand", "dog"]
# s = Solution()
# res = s.wordBreak(string, wordDict)

# string = "pineapplepenapple"
# wordDict = ["apple","pen","applepen","pine","pineapple"]
# s = Solution()
# res = s.wordBreak(string, wordDict)