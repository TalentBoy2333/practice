class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        path = path + '/'
        # 删除所有连续的'/'
        new_path = '/'
        for i in range(1, len(path)):
            if not (path[i] == '/' and path[i-1] == '/'):
                new_path += path[i] 
        # print('删除所有连续的[/]:', new_path)
        # 删除所有'./'
        path = new_path
        new_path = path[:2]
        for i in range(2, len(path)):
            if path[i-2:i+1] == '/./':
                new_path = new_path[:-1]
            else:
                new_path += path[i] 
        # print('删除所有[./]:', new_path)
        # 根据'..'删除之前的路径
        path_list = new_path.split('/')
        # print(path_list)
        ind = 0
        while ind < len(path_list):
            if ind == 1 and path_list[ind] == '..':
                path_list.pop(ind)
            elif path_list[ind] == '..':
                path_list.pop(ind-1)
                path_list.pop(ind-1)
                ind -= 1
            else:
                ind += 1
        # print(path_list)
        new_path = '/'.join(path_list)
        if len(new_path) > 1 and new_path[-1] == '/':
            return new_path[:-1]
        else:
            return new_path

# so = Solution() 
# # s = "/a//b////c/d//././/..///"
# s = "///../../F/./rVH/jmkyl/wpxS/sRC/cL/NR///tO/.//"
# print(s)
# res = so.simplifyPath(s)
# print(res)
