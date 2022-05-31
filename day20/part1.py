def solve(target, limit):
    houses = [1] * target
    for i in range(2, target):
        for j in range(min(target//i, limit)):
            houses[i*j] += i
        if houses[i] >= target:
            return i

with open("input.txt", 'r') as INPUT:
     INPUT = int(INPUT.read())
with open("output1.txt", 'w') as OUTPUT:
    OUTPUT.write(str(solve(INPUT//10, INPUT//10)))

print(solve(INPUT//10, INPUT//10))
