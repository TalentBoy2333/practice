def solution(a):
    """
    思路: 遍历数组, 前三大的数字存入l_max, 前二小的数字存入l_min
         乘积最大只有两种情况: 
         1. l_max中的三个数相乘
         2. l_min的积乘l_max中最大的数
    """
    if(len(a) < 3):
        return 0 
    l_max = []
    l_min = []
    for n in a:
        update_max(n, l_max)
        update_min(n, l_min)
    # print(l_max)
    # print(l_min)
    return max(l_max[0] * l_max[1] * l_max[2], l_min[0] * l_min[1] * l_max[0])

def update_max(num, a):
    if(len(a) < 3):
        a.append(num)
        a.sort(reverse=True)
    elif(num > a[-1]):
        a.pop()
        a.append(num)
        a.sort(reverse=True)
    else:
        return

def update_min(num, a):
    if(len(a) < 2):
        a.append(num)
        a.sort()
    elif(num < a[-1]):
        a.pop()
        a.append(num)
        a.sort()
    else:
        return


if __name__ == '__main__':
    # a = [3,4,1,2]
    # m = solution(a)
    # print(m)

    # a = '3472 -7098 -9281 7789 7955 6101 5051 7778 3090 7423 -7151 5652 1595 -8094 677 -8324 8347 -2482 9313 -9338 -3157 8559 6945 3618 3087 121 -8468 3225 1356 6939 2799 -7231 -6309 -5453 633 -8689 -4776 2714 -2743 -1409 5918 -3333 1803 8330 -2206 -6117 -4486 -7903 -4375 -3739 2897 8056 -5864 -522 7451 -4541 -2813 5790 -532 -6517 925'
    # a = a.split(' ')
    # a = [int(n) for n in a]
    # print(a)
    # print(len(a))
    # print(solution(a))

    n = int(input())
    a = input().split(' ')
    a = [int(n) for n in a]
    print(solution(a))