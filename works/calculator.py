import math
import re

class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def division(self, a, b):
        return a/b

    def sinA(self, a):
        return math.sin(a)

    def cosA(self, a):
        return math.cos(a)

    def tanA(self, a):
        return math.tan(a)

calc = Calculator()

while True:

    print('1: Add')
    print('2: Subtract')
    print('3: Multiply')
    print('4: Divide')
    print('5: Sin function')
    print('6: Cos function')
    print('7: Tan function')
    print('8: Exit')

    num = int(input('Select Operation: '))

    if num in (1, 2, 3, 4, 8):

        if (num == 8):
            break

        a = int(input('Enter first number: '))
        b = int(input('Enter second number: '))

        if(num == 1):
            print(a, '+', b, '=', calc.add(a, b))
        elif(num == 2):
            print(a, '-', b, '=', calc.subtract(a, b))  
        elif(num == 3):
            print(a, '*', b, '=', calc.multiply(a, b))
        elif(num == 4):
            print(a, '/', b, '=', calc.division(a, b))          

    elif num in (5, 6, 7, 8):
    
        if (num == 8):
            break

        a = int(input('Enter radian: ')) 

        if (num == 5):
            print('Sin(a) = ', calc.sinA(a))  
        elif (num == 6):
            print('Cos(a) = ', calc.cosA(a)) 
        elif (num == 7):
            print('Tan(a) = ', calc.tanA(a))         
    
    else:
        print('Invalid input')