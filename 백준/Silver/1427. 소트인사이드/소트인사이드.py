input_str = input()

array = list(input_str)

for i in range(1, len(array)):
    for j in range(i, 0, -1):
        if array[j] > array[j-1]:
            array[j], array[j-1] = array[j-1], array[j]
        else:
            break

print(''.join(array))
