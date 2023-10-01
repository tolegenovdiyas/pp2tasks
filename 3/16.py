queens = []
for _ in range(8):
    queens.append(tuple(map(int, input().split())))
is_conflict = False
for i in range(8):
    for j in range(i + 1, 8):
        if queens[i][0] == queens[j][0] or queens[i][1] == queens[j][1] or abs(queens[i][0] - queens[j][0]) == abs(queens[i][1] - queens[j][1]):
            is_conflict = True
            break
if is_conflict:
    print("YES")
else:
    print("NO")