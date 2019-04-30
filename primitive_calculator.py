# Uses python3
import sys

def optimal_sequence(n):
    pre_num = [-1] * (n + 1)
    allmin_op = [0] + [-1] * n
    
    for i in range(1, n+1):
        now_num = i-1
        now_op = allmin_op[now_num] + 1
        
        if i % 3 == 0:
            num = i // 3
            op = allmin_op[i // 3] + 1
            if op < now_op:
                now_num, now_op = num, op
                
        if i % 2 == 0:
            num = i // 2
            op = allmin_op[i // 2] + 1
            if op < now_op:
                now_num, now_op = num, op
                
        pre_num[i] = now_num
        allmin_op[i] = now_op
        
    sequence = []
    i = n
    while i > 0:
        sequence.append(i)
        i = pre_num[i]
    sequence.reverse()
    
    return sequence

input = sys.stdin.read()
n = int(input)
sequence = list(optimal_sequence(n))
print(len(sequence) - 1)
for x in sequence:
    print(x, end=' ')