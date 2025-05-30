import math

class ShapeCalculator:
    def area(self, a=None, b=None):
        if a is not None and b is None:
            
            return math.pi * a * a
        elif a is not None and b is not None:
            
            return a * b
        else:
            return "Invalid input"

if __name__ == "__main__":
    calc = ShapeCalculator()
    print("Area of Circle (radius=5):", calc.area(5))
    print("Area of Rectangle (5x3):", calc.area(5, 3))
    print("Invalid case (no arguments):", calc.area())
