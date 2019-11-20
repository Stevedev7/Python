special = "!@#$%^&*()-+=:;.,<>?/|\\{}''\"\"`~"

x = input("Enter a string: ")
y = ""
for i in x:
    if i not in special:
        y += i
print(y)
