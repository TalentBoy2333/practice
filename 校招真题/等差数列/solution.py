def solution(x):
    if len(x) <= 2:
        return 'Possible'
    x.sort()
    sub = x[1] - x[0]
    for i in range(2, len(x)):
        if x[i] - x[i-1] != sub:
            return 'Impossible'
    return 'Possible'

if __name__ == '__main__':
    n = int(input())
    x = [int(c) for c in input().split(' ')]
    # print(n)
    # print(x)
    # x = [3,1,2]
    res = solution(x)
    print(res)