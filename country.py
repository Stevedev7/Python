class Country:
    def __init__(self, name, capital, population):
        self.name = name
        self.capital = capital
        self.population = int(population)
    def getPop(self):
        return self.population

def findCapital(list, name):
    for country in list:
        if(country.name == name):
            return country.capital




country = []

while(True):
    choice = input("Enter your choice\n1. Add country\n2. Find capital\n3. Country with heighest population\n4. Exit\n")
    if choice == "1":
        country.append(Country(input("Enter name: "), input("Enter capital: "),input("Enter population: ")))
    elif choice == "2":
        print(findCapital(country,input("Enter Country name: ")))
    elif choice == "3":
        country = sorted(country, key=Country.getPop, reverse=True)
        for i in country:
            print(i.name, i.population)
        if len(country) != 0:
            print("The most populous country is: ", country[0].name, "->", country[0].population,"\n")
        else:
            print("List is empty\n")
    elif choice == "4":
        break
    else:
        print("Invalid choice\n")
