# Uses python3
def evalt(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        assert False
        

        
def MinandMax(i, j, valueM, valuem):
    m = float('inf')
    M = float('-inf')
    for k in range(i, j):
        a = evalt(valueM[i][k], valueM[k+1][j], dataset[2*k+1])
        b = evalt(valueM[i][k], valuem[k+1][j], dataset[2*k+1])
        c = evalt(valuem[i][k], valueM[k+1][j], dataset[2*k+1])
        d = evalt(valuem[i][k], valuem[k+1][j], dataset[2*k+1])
        m = min(m, a, b, c, d)
        M = max(M, a, b, c, d)
    return m, M        



def get_maximum_value(dataset):
#    global valuem
#    global valueM
    n = int((len(dataset) + 1) / 2)
    valuem = [[0 for i in range(n)] for i in range(n)]
    valueM = [[0 for i in range(n)] for i in range(n)]
    for i in range(n):
        valuem[i][i] = dataset[2 * i]
        valueM[i][i] = dataset[2 * i]
    
    for s in range(1, n):
        for i in range(n - s):
            j = i + s
            valuem[i][j], valueM[i][j] = MinandMax(i,j, valueM, valuem)
    return valueM[0][n-1]


if __name__ == "__main__":
    temp = list(input())
    dataset = []
    for i in temp:
        if i.isdigit():
            i = int(i)
        dataset.append(i)
    print(get_maximum_value(dataset))


