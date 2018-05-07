# 버블 정렬
def bubblesort(list): 
    list_len = len(list)
    # range로 인해 인덱스 0부터 1씩 늘려가면서 마지막 인덱스까지 전까지 실행
    # len(list) -1 로 이전 마지막 인덱스 바로 전까지 비교 대상으로 봄
    for i in range(list_len-1):      
        # 비교 인덱스 바로 앞의 요소와 비교 , 크면 유지하고, 작으면 위치를 바꿈
        for j in range(list_len-1-i):
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]
# 삽입 정렬             
def insertionsort(list):
    # 인덱스 0이 아닌 1부터 최종 인덱스까지 비교
    # range 함수로 길이가 5인 list에 인덱스 4까지 1씩 증가되면서 실행
    for i in range(1, len(list)):
        # 바로 옆에 잇는 정렬 목록의 요소와 비교(비교 인덱스 -1 씩 진행)
        j = i-1
        # 임시 변수를 저장해 둔다.
        key = list[i]
        # 정렬된 목록의 요소들과 차례(j--)로 비교하여 적절한 위치에 임시변수 삽입 
        while list[j] > key and j>=0:
            list[j+1] = list[j]
            j = j-1
        # 정렬된 목록의 가장 오른쪽의 요소보다 크다면 정렬된 목록의 비교 과정을 거칠 필요가 없음
        list[j+1] = key

num = int(input())

list = []


for i in range(num):
    list.insert(i,int(input()))
# list.sort()     option으로 reverse = True도 가능
# list.bubblesort()
insertionsort(list)

for i in list:
    print(i)
