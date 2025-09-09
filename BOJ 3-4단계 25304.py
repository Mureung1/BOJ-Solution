total = int(input())
total_count = int(input())
total_sum = 0
for i in range(total_count):
    a, b = map(int, input().split())
    total_sum += a * b

if total == total_sum:
    print("Yes")
else:
    print("No")