# Uses python3
def edit_distance(s, t):
    m, n = len(s), len(t)
    if m == 0:
        return m
    if n == 0:
        return n
    matrix = [[0] * (n + 1) for i in range(0, m + 1)]
    for i in range(1, m + 1):
        matrix[i][0] = i
    for j in range(1, n + 1):
        matrix[0][j] = j
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s[i - 1] == t[j - 1]:
                diff = 0
            else:
                diff = 1
            edit_exchange_dis = matrix[i-1][j-1] + diff
            edit_add_dis = matrix[i-1][j] + 1
            edit_del_dis = matrix[i][j-1] + 1
            matrix[i][j] = min(edit_exchange_dis,edit_add_dis,edit_del_dis)
#            matrix[i][j] = min(matrix[i-1][j], matrix[i][j-1], matrix[i-1][j-1]) + diff
    return matrix[m][n]

if __name__ == "__main__":
    print(edit_distance(input(), input()))
