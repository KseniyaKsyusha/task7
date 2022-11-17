import turtle as t
from random import *


class Figure:

    def __init__(self, side, numberSides, angle):  # конструктор
        self.verify_side(side)
        self.verify_numberSides(numberSides)
        self.verify_angle(angle)

        self.__side = side
        self.__numberSides = numberSides
        if angle == 0:
            self.__angle = 180 - 180 * (self.__numberSides - 2) / self.__numberSides
        else:
            self.__angle = angle

    @classmethod
    def verify_side(cls, side):
        if type(side) != int:
            raise TypeError("Довжина боку фігури має бути цілим числом!!")

    @classmethod
    def verify_numberSides(cls, numberSides):
        if type(numberSides) != int or numberSides < 3 or numberSides > 10:
            raise TypeError("Кількість сторін фігури має бути цілим числом і набувати значень від 3 до 5!!")

    @classmethod
    def verify_angle(cls, angle):

        if type(angle) != int or angle < -180 or angle > 180:
            raise TypeError("Кут набуває значень від -180 до 180 градусів")

    @property
    def side(self):  # геттеры
        return self.__side

    @side.setter
    def side(self, side):
        self.verify_side(side)
        self.__side = side

    @property  # декоратор
    def numberSides(self):
        return self.__numberSides

    @numberSides.setter
    def numberSides(self, numberSides):
        self.verify_numberSides(numberSides)
        self.__numberSides = numberSides

    @property
    def angle(self):
        return self.__angle

    @angle.setter
    def angle(self, angle):
        self.verify_angle(angle)

        if angle == 0:
            self.__angle = 180 - 180 * (self.__numberSides - 2) / self.__numberSides
        else:
            self.__angle = angle

    def draw(self):  # название фнкции и три параметра передаются
        t.TurtleScreen._RUNNING = True
        t.speed(0)
        t.width(5)
        t.pu()
        t.goto(-100, 100)
        t.pd()
        t.color("#%03x" % randint(0, 0xFFF))
        t.begin_fill()
        for i in range(self.__numberSides):
            t.forward(self.__side)
            t.right(self.__angle)
        t.end_fill()
        t.exitonclick()
