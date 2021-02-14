import unittest
from work_calc import Calc
from hard_Calc import Calc_hard, Calc_hard2

class SimpleCalcTest(unittest.TestCase):
    # def setUp(self):
    #     self.calculator = Calc()
    
    # def tearDown(self):
    #     pass
    a = 7
    b = 4

    def test_add(self):
        res = Calc.add(7, 4)
        exp_res = 7+4
        self.assertEqual(res, exp_res, 'Good job')

    def test_minus(self):
        res = Calc.min(7, 4)
        exp_res = 7-4
        self.assertEqual(res, exp_res, 'Good job')

    def test_multiply(self):
        res = Calc.mult(7, 4)
        exp_res = 7*4
        self.assertEqual(res, exp_res, 'Good job')

    def test_divide(self):
        res = Calc.div(7, 4)
        exp_res = 7/4
        self.assertEqual(res, exp_res, 'Good job')

    def test_div_end(self):
        res = Calc.div_end(7, 4)
        exp_res = 7//4
        self.assertEqual(res, exp_res, 'Good job')

    def test_degree(self):
        res = Calc.degree(7, 4)
        exp_res = 7**4
        self.assertEqual(res, exp_res, 'Good job')

class SimpleCalcTest1(unittest.TestCase):

    def test_polish(self):
        res = Calc_hard.polish_rec('14+5/2-96*147')
        exp_res = '14 5 2 96 147 + / - *'
        self.assertEqual(res, exp_res, 'Good job')
        

class SimpleCalcTest2(unittest.TestCase):

    def test_polish_rev(self):
        res = Calc_hard2.polish_rec(['14', '25', '1.2', '77777'], ['/', '-', '+'])
        exp_res = '14/25-1.2+77777'
        self.assertEqual(res, exp_res, 'Good job')

if __name__ == '__main__':
    unittest.main()