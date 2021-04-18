"""이겄은 함수를 이용한 퀴즈 입니다."""

score=0
q1=['''첫번째 문제''','''두번쩨문제''','''세번쩨문제''']

def clac(answer, sol):
    global score
    if answer == sol:
        score = score + 1
    return

"""1번 문제에 대한 코드"""

print(q1[0])
clac(int(input()), 2)
print(score)

"""2번 문제에 대한 코드"""

print(q1[1])
clac(int(input()), 3)
print(score)
