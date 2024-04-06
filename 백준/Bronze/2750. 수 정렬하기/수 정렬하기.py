n = int(input())  # 수의 개수 입력
array = [int(input()) for _ in range(n)]  # 수 입력

stack = [(0, len(array) - 1)]

while stack:
    start, end = stack.pop()
    if start >= end:  # 부분 배열의 길이가 1 이하면 다음으로
        continue
    
    pivot = array[(start + end) // 2]  # 피벗은 중앙 값
    left, right = start, end
    
    while left <= right:
        while array[left] < pivot:  # 피벗보다 크거나 같은 값을 찾음
            left += 1
        while array[right] > pivot:  # 피벗보다 작거나 같은 값을 찾음
            right -= 1
        
        if left <= right:  # 교차되지 않았다면 요소 교환
            array[left], array[right] = array[right], array[left]
            left, right = left + 1, right - 1
    
    stack.append((start, right))  # 왼쪽 부분 배열 다시 처리
    stack.append((left, end))  # 오른쪽 부분 배열 다시 처리

# 정렬된 배열 출력
for num in array:
    print(num)
