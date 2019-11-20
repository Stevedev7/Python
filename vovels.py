vove = {}

vove["a"] = 0
vove["e"] = 0
vove["i"] = 0
vove["o"] = 0
vove["u"] = 0

string = input("Enter a string: ")
string = string.lower()

for i in string:
    for j in vove:
        if (i == j):
            vove[i] += 1

print(vove)
