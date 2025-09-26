N, M = map(int, input().split(" "))
cards = list(map(int, input().split(" ")))
total = 0
for i in range(len(cards)):
    for j in range(i+1, len(cards)):
        for k in range(j+1, len(cards)):
            if cards[i] + cards[j] + cards[k] > M:
                continue
            else:
                # total과 세 숫자의 합을 비교하여 더 큰 수를 total에 저장한다.
                # for문을 돌면서 M보다 작거나 같은 값 중 가장 큰 수를 찾는다.
                total = max(total, cards[i] + cards[j] + cards[k])

print(total)