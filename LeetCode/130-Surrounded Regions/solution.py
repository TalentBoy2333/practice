class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        if board == []:
            return 
        loaded = [[] for _ in range(len(board))]
        # 创建访问字典
        for temp in loaded:
            for i in range(len(board[0])):
                temp.append(0)
        # print(loaded)
        '''
        问题转化为, 如何寻找和边界联通的'O': 
        '''
        bdy_list = list() # 用于保存连通到边界的'O'区域
        # 第一行和最后一行
        for i in [0, len(loaded)-1]:
            for j in range(len(loaded[0])):
                if loaded[i][j] == 0: # 如果没被访问过
                    self.part(board, loaded, bdy_list, i, j)
        # 第一列和最后一列
        for j in [0, len(loaded[0])-1]:
            for i in range(len(loaded)):
                if loaded[i][j] == 0: # 如果没被访问过
                    self.part(board, loaded, bdy_list, i, j)
        # print(bdy_list)
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'O' and (i, j) not in bdy_list:
                    board[i][j] = 'X'


    def part(self, board, loaded, bdy_list, x, y):
        if loaded[x][y] == 1:
            return 
        loaded[x][y] = 1
        if board[x][y] == 'O':
            print(x,y)
            bdy_list.append((x, y))
            if x > 0:
                self.part(board, loaded, bdy_list, x-1, y)
            if x < len(board)-1:
                self.part(board, loaded, bdy_list, x+1, y)
            if y > 0:
                self.part(board, loaded, bdy_list, x, y-1)
            if y < len(board[0])-1:
                self.part(board, loaded, bdy_list, x, y+1)

# def show(board):
#     for l in board:
#         print(l)
#     print()

# if __name__ == '__main__':
#     # board = [['X', 'X', 'X', 'X'], 
#     #          ['X', 'O', 'O', 'X'],
#     #          ['X', 'X', 'O', 'X'],
#     #          ['X', 'O', 'X', 'X']]
#     board = [["X","O","O","X","X","X","O","X","O","O"],["X","O","X","X","X","X","X","X","X","X"],["X","X","X","X","O","X","X","X","X","X"],["X","O","X","X","X","O","X","X","X","O"],["O","X","X","X","O","X","O","X","O","X"],["X","X","O","X","X","O","O","X","X","X"],["O","X","X","O","O","X","O","X","X","O"],["O","X","X","X","X","X","O","X","X","X"],["X","O","O","X","X","O","X","X","O","O"],["X","X","X","O","O","X","O","X","X","O"]]
#     show(board)
#     so = Solution()
#     so.solve(board)
#     show(board)
        