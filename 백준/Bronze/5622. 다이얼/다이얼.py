dial = ['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']

word = input()
second=0

for ch in word: #단어를 리스트 처럼 뽑아준다.
    for i in range(len(dial)):
        if ch in dial[i]: # 'A' in 'ABC'
            i+=3
            second+=i
print(second)
