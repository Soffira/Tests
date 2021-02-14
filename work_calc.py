import re
def check_correct(exampleA):
    if exampleA.startswith(('+', '*', '/', '(', ')')):
        return False
    elif not re.match(r'[\d.]+|[\+\-\/\*\(\)]', exampleA, re.IGNORECASE):
        return False
    else:
        return True

class Calc():
    
    def __init__(self):
        pass
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def min(a, b):
        return a - b

    @staticmethod    
    def mult(a, b):
        return a * b
    
    @staticmethod
    def div(a, b):
        if b != 0:
            return a / b
        else:
            print('You can not divide by 0')
            return False
    
    @staticmethod
    def div_end(a, b):
        if b != 0:
            return a // b
        else:
            print('You can not divide by 0')
            return False
    
    @staticmethod
    def degree(a, b):
        return a ** b


if __name__ == '__main__':
    exampleA = input('Enter an example: ')
    example = exampleA.replace(' ', '')
    patt = '(\-?\d+\.?\d*)(\+|\-|\*|\/|\//|\**)(\-?\d+\.?\d*)'
    res_examle = re.findall(patt, example)

    a = int(res_examle[0][0])    
    b = int(res_examle[0][2])
    sign = res_examle[0][1]

    if check_correct(exampleA) == True:
        calculator = Calc()
        if sign == '+':
            print(calculator.add(a, b))
        elif sign == '-':
            print(calculator.min(a, b))
        elif sign == '/':    
            print(float(calculator.div(a, b)))
        elif sign == '*':
            print(calculator.mult(a, b))
        elif sign == '//':
            print(calculator.div_end(a, b))
        elif sign == '**':
            print(calculator.degree(a, b))
    else:
        print('The expression is not correct')

    # Calc.add(23, 55.0)