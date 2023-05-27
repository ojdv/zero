#相較講義更簡潔
scores = []
for i in range(2):
    a = sum(map(int, input().split()))
    b = sum(map(int, input().split()))
    scores.append(a > b)
    print(f"{a}:{b}")

if all(scores):
    print("Win")
elif not all(scores):
    print("Lose")