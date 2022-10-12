import unittest
import tz2

from functools import reduce

class Testing(unittest.TestCase):
    if len(tz2.sp1) != 0:
        def test_min(self):
            answer = tz2._min(tz2.sp1)
            self.assertEqual(answer, min(tz2.sp1))
        def test_max(self):
            answer2 = tz2._max(tz2.sp1)
            self.assertEqual(answer2, max(tz2.sp1))
        def test_sum(self):
            answer3 = tz2._sum(tz2.sp1)
            self.assertEqual(answer3, sum(tz2.sp1))
        def test_mult(self):
            answer4 = tz2._mult(tz2.sp1)
            self.assertEqual(answer4, reduce((lambda x,y: x * y), tz2.sp1))
        def test_my(self):
            answer5 = tz2._max(tz2.sp1) * tz2._min(tz2.sp1)
            self.assertEqual(answer5, max(tz2.sp1) * min(tz2.sp1))
    else:
        def test_min1(self):
            answer6 = tz2._min(tz2.sp1)
            self.assertEqual(answer6, None)
        def test_max1(self):
            answer7 = tz2._max(tz2.sp1)
            self.assertEqual(answer7, None)
        def test_sum1(self):
            answer8 = tz2._sum(tz2.sp1)
            self.assertEqual(answer8, None)
        def test_mult1(self):
            answer9 = tz2._mult(tz2.sp1)
            self.assertEqual(answer9, None)
        def test_my1(self):
            answer10 = tz2.minef(tz2.sp1)
            self.assertEqual(answer10, None)
    def test_Time(self):
        print('Время работы программы:', tz2.c.microseconds, 'микросекунд', 'или', tz2.c.microseconds / 1000000, 'секунд')
if __name__ == '__main__':
    unittest.main()
