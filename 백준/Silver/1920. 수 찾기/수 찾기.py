def binary_serch(target, array):
    min_num = 0
    max_num = n-1
    cursor = (min_num+max_num)//2

    while min_num <= max_num:
        if array[cursor] == target:
            return 1
        elif array[cursor] < target:
            min_num = cursor +1
        elif array[cursor] > target:
            max_num = cursor -1
        
        cursor = (max_num +min_num)//2
    return 0


n = int(input())
n_array = list(map(int, input().split()))
n_array.sort()

m =  int(input())
m_array = list(map(int, input().split()))

for i in m_array:
    print(binary_serch(i,n_array))