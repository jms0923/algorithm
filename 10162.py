time = int(input())                                     # 입력 받은 시간
remainTime = time                                       # 계산해서 저장할 남은 시간 벼누

buttonA = 0                                             # 버튼 A는 5분이니 300초 -> 단위 통일
buttonB = 0                                             # 버튼 B는 1분이니 60초
buttonC = 0                                             # 버튼 C는         10초

while True:                                             # 조건을 만족할 때 까지 반복(1)
    if remainTime >= 300:                               # 버튼 A가 단위가 제일 크므로, 가장 많이 할당되어야 함.
        buttonA = remainTime // 300                     # 버튼 A를 최대 몇번 누를 수 있는가 -> 남은 시간에서 5분으로 나눈 몫만 저장
        remainTime = remainTime - (buttonA * 300)       # 버튼 A를 누르고 남은 시간은 몇 초인가? -> 버튼 A를 눌러 감소된 시간 만큼 빼줌

    if remainTime >= 60:
        buttonB = remainTime // 60
        remainTime = remainTime - (buttonB * 60)

    if remainTime >= 10:
        buttonC = remainTime // 10
        remainTime = remainTime - (buttonC * 10)

    elif remainTime < 10:                               # (1) while 종료 조건
        break


if remainTime == 0:                                     # 남은 시간이 없도록 딱 맞춰 눌렀을 경우 -> 각 버튼당 눌린 횟수 출력
    print(buttonA, buttonB, buttonC)

else:                                                   # 남은 시간이 맞아 떨어지지 않을 경우 -> -1 출력
    print(-1)
