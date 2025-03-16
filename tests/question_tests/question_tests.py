#write function tests here, don't add input('') statements here!
import unittest

#follow this example to add questions b, c, and d for testing including their functions
from src.question_b.question_b import get_sum_of_evens

class Test_Config(unittest.TestCase):

    def test_get_sum_of_evens(self):
        self.assertEqual(get_sum_of_evens(10), 30)
        self.assertEqual(get_sum_of_evens(8), 20)

import unittest
from src.question_c.question_c import reverse_string
class Test_Config(unittest.TestCase):
    def test_reverse_string(self):
        self.assertEqual(reverse_string('hello'), 'olleh')
        self.assertEqual(reverse_string('hello world'), 'dlrow olleh')

import unittest
from src.question_a.question_a import get_person_category
class Test_Config(unittest.TestCase):
    def test_get_person_category(self):
        self.assertEqual(get_person_category(1), "infant")
        self.assertEqual(get_person_category(2), "child")
        self.assertEqual(get_person_category(14), "teenager")
        self.assertEqual(get_person_category(20), "adult")

import unittest
from src.question_d.question_d import get_bonus_pay_amount
class Test_Config(unittest.TestCase):
    def test_get_bonus_pay_amount(self):
        self.assertEqual(get_bonus_pay_amount(200), 10)
        self.assertEqual(get_bonus_pay_amount(600), 36)
        self.assertEqual(get_bonus_pay_amount(1000), 70)
        self.assertEqual(get_bonus_pay_amount(1500), 120)
        self.assertEqual(get_bonus_pay_amount(2000), "Invalid number")