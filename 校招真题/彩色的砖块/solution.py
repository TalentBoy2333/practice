def solution(s):
    """
    对每种颜色砖块个数做统计: 
    1. 如果出现了两种以上的颜色, 肯定最少有两种相邻，直接输出0.
    2. 如果出现了一种, 那就只有一种.
    3. 如果出现了两种, 那就只有两种. 
    """
    char_cls = []
    for c in s:
        if c not in char_cls:
            char_cls.append(c)
    # print(char_cls)
    if len(char_cls) > 2:
        return 0
    elif len(char_cls) == 1:
        return 1
    else:
        return 2

# def solution(s):
#     l = []
#     permutation(s, 0, l)
#     # print(l)
#     count = 0
#     for ps in l:
#         if is_nice(ps):
#             # print(ps)
#             count += 1
#     return count

# def is_nice(s):
#     count = 0
#     for i in range(1, len(s)):
#         if s[i-1] != s[i]:
#             count += 1
#     if count < 2:
#         return True
#     else:
#         return False

# # 全排列(去重)
# def permutation(s, index, l):
#     if len(s) == index:
#         l.append(s.copy())
#     for i in range(index, len(s)):
#         if is_swap(s, index, i):
#             swap(s, i, index)
#             permutation(s, index+1, l)
#             swap(s, i, index)
# def swap(s, x, y):
#     temp = s[x]
#     s[x] = s[y]
#     s[y] = temp
# def is_swap(s, index, x):
#     for i in range(index, x):
#         if(s[i] == s[x]):
#             return False
#     return True

if __name__ == '__main__':
    # s = list('abab')
    # solution(s)

    s = list(input())
    print(solution(s))