import sys

def Mergesort(list):
    # 베이스 케이스(base case)
    if len(list) <= 1:
        return list
    # 주어진 초기의 리스트를 반으로 나눈다. 단 나머직 없도록 // 을 사용한다.
    mid = len(list) // 2
    # 가운데르 기준으로 왼쪽, 오른쪽으로 리스트를 나눈다.
    left = list[:mid]
    right = list[mid:]
    # 왼쪽부터 잘라진 리스트들을 Recursive call 해주고, 매번 반으로 잘라 준다.
    next_left = Mergesort(left)
    next_right = Mergesort(right)
    # 나눌 수 없을 때까지 반으로 쪼갠 후에 분할을 마친다.
    # 이를 합병 함수로 보낸다.
    return Merge(next_left, next_right)

def Merge(left, right): # 쪼개진 리스트를 합병하는 함수
    # 초기 인덱스 및 결과 리스트 설정
    i = 0
    j = 0
    sorted_list = []
    # 잘려진 부분이 비어 있는 경우가 아닐 경우나 합병 과정에서 길이가 늘어가기에 합병이 잘 되고 있다는 것도 확인
    # 왼쪽과 오른쪽 부분이 모두 합병이 되어 1씩 증가하는 인덱스 보다 더 클 경우
    # 즉 합병이 가능한 경우(왼쪽, 오른쪾 리스트에 원소들이 채워져 있는 경우)
    while (i < len(left)) & (j < len(right)):
        # 왼쪽 리스트의 첫 인덱스가 더 작을 경우, 결과 리스트에 왼쪽 리스트의 해당 값을 넣는다.
        if left[i] < right[j]:
            sorted_list.append(left[i])
            # 왼쪽의 첫번쨰가 들어갔기에 인덱스 번호를 하나 늘려 옆으로 이동
            i += 1
        else: # 오른쪾의 작을 경우도 위와 마찬가지로 진행
            sorted_list.append(right[j])
            j += 1
    # 왼쪽 리스트에만 원소가 있고, 오른쪾 리스트는 비어 있는 상황
    while i < len(left):
        # 정렬 되어있단 가정 하에 그냥 순서대로 넣는다.
        sorted_list.append(left[i])
        i += 1
    # 오른쪽 리스트에만 원소가 있고, 오른쪽 리스트는 비어 있는 상황
    while j < len(right):
        sorted_list.append(right[j])
        j += 1
    return sorted_list
# 파이썬 속도를 높이기 위한 터미널 딴에 입력 
num = int(sys.stdin.readline())
list = []
for i in range(num):
    list.append(int(sys.stdin.readline()))
a = Mergesort(list)
for i in a:
    print(i)
