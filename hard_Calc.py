import re
def check_correct(exampleA):
    if exampleA.startswith(('+', '*', '/', '(', ')', '.')):
        return False
    elif not re.match(r'[\d.]+|[\+\-\/\*]', exampleA, re.IGNORECASE):
        return False
    else:
        return True


class Calc_hard():
    def __init__(self):
        pass
    
    @staticmethod
    def polish_rec(example):
        ints = []
        signs = []
        num_less = len(example)
        num = ''
        sign = ''
        for i in example:
            num_less -= 1
            if i.isdigit() and num_less != 0:
                num += i
            elif i.isdigit() and num_less == 0:
                num += i
                ints.append(num)
            elif i == '.':
                 num += i
            else:
                ints.append(num)
                num = ''
                signs.append(i)
        result = (' '.join(ints) + ' ' + ' '.join(signs))
        # return ints, signs
        return result
        # print(' '.join(ints) + ' ' + ' '.join(signs))    

class Calc_hard2():
    def __init__(self):
        pass
    
    @staticmethod
    def polish_rec(ints, signs):
        origin_res = ''
        s = 0
        for i in ints:
            if i != ints[-1]:
                origin_res += i
                origin_res += signs[s]
                s += 1
            else:
                origin_res += i
        return origin_res
    # print(origin_res)


if __name__ == '__main__':
    quest = input('If you want to get Polish record, please write 1, for getting the original expression from Polish record write 2: ')
    
    if quest == '1':
        exampleA = input('Enter an example for Polish record: ')
        example = exampleA.replace(' ', '')
        if check_correct(example) == True:
            calculator = Calc_hard()
            print(calculator.polish_rec(example))
        else:
            print('The expression is not correct')
    
    elif quest == '2':
        exampleA = input('Enter a Polish record: ')
        example = exampleA.split()
        ints = []
        signs = []
        for c in example:
            if c.isdigit() or '.' in c:
                ints.append(c)
            elif c == '+' or c == '-' or c == '/' or c == '*':
                signs.append(c)
        if check_correct(exampleA) == True:
            calculator = Calc_hard2()
            print(calculator.polish_rec(ints, signs))
        else:
            print('The expression is not correct')
    
    else:
        print('You did not choose any option')
    
    # print(' '.join(ints) + ' ' + ' '.join(signs))2
    
