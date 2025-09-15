import string

S =input()
lower = list(string.ascii_lowercase)
result = []
for ch in lower :
    #있는 알파벳이라면 위치
    if ch in S:
        result.append(S.index(ch))
    #없다면 -1
    else:
        result.append(-1)

print(*result) #result의 모든 요소 공백으로 펼쳐서 출력