# Uses python3
import sys

def get_number_of_inversions(a, left, right):
    number_of_inversions = 0
    if right - left <= 1:
        return number_of_inversions
    else:
        ave = (left + right) // 2
        number_of_inversions += get_number_of_inversions(a, left, ave)
        number_of_inversions += get_number_of_inversions(a, ave, right)
        lst1= a[left:ave]
        lst2 = a[ave:right]
        lst1.sort()
        lst2.sort()
        i = 0
        j = 0
        while i < len(lst1) and j < len(lst2):
            if lst1[i] <= lst2[j]:
                i += 1
            else:
                number_of_inversions += len(lst1) - i
                j += 1
    return number_of_inversions

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    b = n * [0]
    print(get_number_of_inversions(a, 0, len(a)))
