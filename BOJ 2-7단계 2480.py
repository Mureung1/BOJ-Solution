a, b, c = map(int, input().split())
prize = 0

# 같은 눈이 3가지 일때
if a == b and b == c:
    prize = 10000 + (a*1000)

# 같은 눈이 2가지 일때
elif a == b:
    prize = 1000 + (a * 100)
elif b == c:
    prize = 1000 + (b * 100)
elif a == c:
    prize = 1000 + (a * 100)

# 모두 다른 눈이 나오는 경우
else:
    prize = max(a, b, c) * 100

print(prize)