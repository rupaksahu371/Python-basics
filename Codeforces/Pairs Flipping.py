import sys
input = sys.stdin.readline

t = int(input())

out_lines = []

for _ in range(t):
    n = int(input())
    line = input().strip()
    # Ensure we have exactly n characters
    if len(line) < n:
        # Pad with zeros if too short
        line = line + '0' * (n - len(line))
    elif len(line) > n:
        # Truncate if too long
        line = line[:n]
    s = list(line)

    k = n // 2
    ans = []

    for x in range(1, k + 1):
        left = x - 1
        right = n - x

        if s[left] != s[right]:
            # choose l = left
            ans.append(left)
            # flip both
            s[left] = '1' if s[left] == '0' else '0'
            s[right] = '1' if s[right] == '0' else '0'
        # else: do nothing when characters are already equal

    out_lines.append(" ".join(map(str, ans)))

print("\n".join(out_lines))
