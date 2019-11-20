n = int(input("Enter n: "))

f1 = 0
f2 = 1

print(f1, "\n"+str(f2))

for i in range(2, n):
    f3 = f1 + f2
    print(f3)
    f1 = f2
    f2 = f3
