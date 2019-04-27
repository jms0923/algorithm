roundNum = int(input())                                         # 라운드 수

for i in range(roundNum):                                       # 라운드 수 만큼 반복
    aPictureList = list(map(int, input().split()))              # A의 그림 정보 입력 받음 - 리스트
    bPictureList = list(map(int, input().split()))              # B의 그림 정보 입력 받음 - 리스트
                                                                # pop(0) - 리스트에서 가장 앞의 값을 꺼냄
    aPictureNum = aPictureList.pop(0)                           # A의 그림의 개수 - 리스트의 가장 앞 숫자
    bPictureNum = bPictureList.pop(0)                           # B의 그림의 개수 - 리스트의 가장 앞 숫자
                                                                # pop() - 리스트에서 가장 뒤의 값을 꺼냄
    aPictureNumList = [0, 0, 0, 0]                              # A가 어떤 그림을 몇개 가지고 있는지 담을 리스트
    bPictureNumList = [0, 0, 0, 0]                              # B가 어떤 그림을 몇개 가지고 있는지 담을 리스트

    for k in range(aPictureNum):                                # A의 그림 정보를 하나씩 꺼내서 어떤 그림인지 확인
        nowAPicture = aPictureList.pop(0)                       # 그림 하나 꺼내기
        if 4 == nowAPicture:                                    # 꺼낸 그림이 4면 별표 - aPictureNumList[0]
            aPictureNumList[0] = aPictureNumList[0] + 1
        elif 3 == nowAPicture:                                  # 꺼낸 그림이 3이면 별표 - aPictureNumList[1]
            aPictureNumList[1] = aPictureNumList[1] + 1
        elif 2 == nowAPicture:                                  # 꺼낸 그림이 2면 별표 - aPictureNumList[2]
            aPictureNumList[2] = aPictureNumList[2] + 1
        elif 1 == nowAPicture:                                  # 꺼낸 그림이 1이면 별표 - aPictureNumList[3]
            aPictureNumList[3] = aPictureNumList[3] + 1

    for l in range(bPictureNum):                                # B도 A와 같이 반복
        nowBPicture = bPictureList.pop(0)
        if 4 == nowBPicture:
            bPictureNumList[0] = bPictureNumList[0] + 1
        elif 3 == nowBPicture:
            bPictureNumList[1] = bPictureNumList[1] + 1
        elif 2 == nowBPicture:
            bPictureNumList[2] = bPictureNumList[2] + 1
        elif 1 == nowBPicture:
            bPictureNumList[3] = bPictureNumList[3] + 1

    for j in range(4):                                          # 그림이 총 4종류니까 최대 4번만 비교하면 됨
        if aPictureNumList[j] > bPictureNumList[j]:             # 각 4종류의 그림이 몇개씩 들어있는지 적혀있는 aPictureNumList를 차례로 확인
            print('A')                                          # A가 더 크면 출력하고 반복문 하나만 종료
            break
        elif aPictureNumList[j] < bPictureNumList[j]:           # B가 더 클 경우
            print('B')
            break                                               # A와 B가 같은 경우는 아무것도 하지 않음
        if j == 3:                                              # 4가지 그림을 모두 확인했는데, 모두 같은 개수일 경우 무승부
            print('D')
            break
