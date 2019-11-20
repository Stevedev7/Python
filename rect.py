class Rectangle:
    def __init__(self, width, height):
        self.width = int(width)
        self.height = int(height)

    def area(self):
        return self.height * self.width

rect = []

n = int(input("Enter the number of rect: "))

for i in range(0, n):
    rect.append(Rectangle(input("Length: "), input("breadth: ")))

rect = sorted(rect, key = Rectangle.area)

print(rect[-1].height, rect[-1].width)
print(rect[0].height, rect[0].width)
