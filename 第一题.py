def solve(source, target):
    # n 行 m 列
    n = len(source)
    m = len(target)
    s = set()
    for x in source:
        s.add(x)

    for x in target:
        if x not in s:
            return -1;

    dp = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if (source[i] == target[j]):
                dp[i][j] = 1

    l = []
    for j in range(m):
        for i in range(n):
            if dp[i][j] == 1:
                l.append(i);
                break
    ans = 0
    for i in range(1, len(l)):
        if l[i] > l[i - 1]:
            continue
        ans += 1
    return ans + 1


if __name__ == '__main__':
    print(solve("abc", "abcbc"))
    print(solve("abc", "acdbc"))
    print(solve("xyz", "xzyxz"))
