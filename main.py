from Figure import Figure
from Square import Square
from Draw import Draw

if __name__ == '__main__':
    obj = Figure(100, 5, 144)
    obj.draw()

    obj2 = Figure(100, 3, -120)
    obj2.draw()

    obj1 = Draw(150, 6)
    obj1.angle = 0
    obj1.draw()

    obj1 = Draw(100, 7)
    obj1.draw()

    obj3 = Square(150)
    obj3.draw()

    obj4 = Square(150.6)
    obj4.draw()
