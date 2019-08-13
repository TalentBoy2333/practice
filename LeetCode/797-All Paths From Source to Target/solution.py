class Solution(object):
    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        self.res = list() 
        target = len(graph) - 1
        self.part(graph, target, graph[0], [0])
        return self.res
        

    def part(self, graph, target, p_list, li):
        for element in p_list:
            cur_list = li[:]
            cur_list.append(element)
            if element == target:
                self.res.append(cur_list)
            else:
                self.part(graph, target, graph[element], cur_list)



# if __name__ == '__main__':
#     graph = [[1,2], [3], [3], []] 
#     so = Solution()
#     res = so.allPathsSourceTarget(graph)
#     print(res)
