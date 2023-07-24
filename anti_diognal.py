def diagonal(A, n):
    for x in range(n):
        i = x
        j = 0
        while i >= 0 and j < n:
            print(A[j][i], end="")
            i -= 1
            j += 1
        print()
    for y in range(1, n):
        i = y
        j = n - 1
        while i < n and j >= 0:
            print(A[i][j], end="")
            j -= 1
            i += 1
    print()

n = int(input())
arr = []
for i in range(n):
    row = list(map(int, input().split()))
    arr.append(row)

diagonal(arr, n)
