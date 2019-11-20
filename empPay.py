def payCheck():
    name = input("Empoloyee name: ")
    n = int(input("Empoloyee hours worked per week: "))
    w = int(input("Empoloyees week: "))
    rate = int(input("Empoloyee rate: "))

    salary = n * rate * w

    print(name, n, w, rate, salary)

payCheck()
