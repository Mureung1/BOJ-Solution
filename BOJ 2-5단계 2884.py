H, M = map(int, input().split())

if M < 45:
    H -= 1  # 시간을 1시간 앞으로
    M += 15 # M = M + 60 - 45 와 동일
    
    if H < 0: # 만약 시간이 -1이 되었다면
        H = 23 # 23시로 변경
else: # M이 45분 이상이라면
    M -= 45 # 분만 45 빼주기

print(H, M)