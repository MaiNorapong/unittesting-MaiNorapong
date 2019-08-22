import math
import unittest
from fraction import Fraction


class FractionTest(unittest.TestCase):
    """Test the methods and constructor of the Fraction class. """

    def test_str(self):
        f = Fraction(3, -1)
        self.assertEqual("-3", f.__str__())
        f = Fraction(0, 5)
        self.assertEqual("0", f.__str__())
        f = Fraction(60, 90)
        self.assertEqual("2/3", f.__str__())
        f = Fraction(1500, 60)
        self.assertEqual("25", f.__str__())
        f = Fraction(1500, 90)
        self.assertEqual("50/3", f.__str__())
        f = Fraction(-80, 20)
        self.assertEqual("-4", f.__str__())
        f = Fraction(36, -60)
        self.assertEqual("-3/5", f.__str__())
        # Constructor should provide default denominator = 1
        f = Fraction(99)
        self.assertEqual("99", f.__str__())

        f = Fraction(1, 0)
        self.assertEqual("1/0", f.__str__())
        f = Fraction(-1, 0)
        self.assertEqual("-1/0", f.__str__())
        f = Fraction(0, 0)
        self.assertEqual("0/0", f.__str__())

    def test_float(self):
        self.assertEqual(0.0, Fraction(0).__float__())
        self.assertEqual(math.inf, Fraction(5, 0).__float__())
        self.assertEqual(13 / 7, Fraction(13, 7).__float__())
        self.assertEqual(42 / 28, Fraction(42, 28).__float__())
        self.assertEqual(-3.0, Fraction(-3).__float__())
        self.assertEqual(2 / -5, Fraction(2, -5).__float__())
        self.assertEqual(-2 / -5, Fraction(-2, -5).__float__())
        self.assertEqual(-math.inf, Fraction(-2, 0).__float__())
        self.assertEqual(2.4 / -3.6, Fraction(2.4, -3.6).__float__())
        self.assertTrue(math.isnan(Fraction(0, 0).__float__()))

    def test_init(self):
        # zero numerator
        f = Fraction(0)
        self.assertEqual(0, f.numerator)
        self.assertEqual(1, f.denominator)
        # zero denominator
        f = Fraction(5, 0)
        self.assertEqual(1, f.numerator)
        self.assertEqual(0, f.denominator)
        # no common factor
        f = Fraction(13, 7)
        self.assertEqual(13, f.numerator)
        self.assertEqual(7, f.denominator)
        # yes common factor
        f = Fraction(42, 28)
        self.assertEqual(3, f.numerator)
        self.assertEqual(2, f.denominator)
        # negative numerator
        f = Fraction(-3)
        self.assertEqual(-3, f.numerator)
        self.assertEqual(1, f.denominator)
        # negative denominator
        f = Fraction(2, -5)
        self.assertEqual(-2, f.numerator)
        self.assertEqual(5, f.denominator)
        # both negative
        f = Fraction(-2, -5)
        self.assertEqual(2, f.numerator)
        self.assertEqual(5, f.denominator)
        # negative infinity
        f = Fraction(-2, 0)
        self.assertEqual(-1, f.numerator)
        self.assertEqual(0, f.denominator)
        # float
        f = Fraction(2.4, -3.6)
        self.assertEqual(-2, f.numerator)
        self.assertEqual(3, f.denominator)
        # zero over zero
        f = Fraction(0, 0)
        self.assertEqual(0, f.numerator)
        self.assertEqual(0, f.denominator)
        # inf float
        f = Fraction(math.inf)
        self.assertEqual(1, f.numerator)
        self.assertEqual(0, f.denominator)
        f = Fraction(-math.inf)
        self.assertEqual(-1, f.numerator)
        self.assertEqual(0, f.denominator)
        # nan float
        f = Fraction(math.nan)
        self.assertEqual(0, f.numerator)
        self.assertEqual(0, f.denominator)
        # invalid type
        with self.assertRaises(TypeError):
            Fraction('two over eight')
        # Constructor should provide default denominator = 1
        f = Fraction(99)
        self.assertEqual(99, f.numerator)
        self.assertEqual(1, f.denominator)

    def test_add(self):
        # 3/4 = 2/3 + 1/12
        self.assertEqual(Fraction(3, 4), Fraction(1, 12) + Fraction(2, 3))
        self.assertEqual(Fraction(3, 7), Fraction(1, 7) + Fraction(2, 7))

        self.assertEqual(Fraction(1, 0), Fraction(1, 0) + Fraction(100, 7))
        self.assertEqual(Fraction(-1, 0), Fraction(-1, 0) + Fraction(100, 7))
        # inf + inf
        self.assertEqual(Fraction(1, 0), Fraction(1, 0) + Fraction(1, 0))
        # inf - inf -> indeterminate
        self.assertTrue((Fraction(1, 0) + Fraction(-1, 0)).isnan())

        # other types
        self.assertEqual(Fraction(11, 4), Fraction(3, 4) + 2)
        self.assertEqual(Fraction(71, 20), Fraction(3, 4) + 2.8)
        self.assertEqual(Fraction(1, 0), Fraction(3, 4) + math.inf)
        self.assertTrue((Fraction(1) + math.nan).isnan())
        with self.assertRaises(TypeError):
            Fraction(3, 4) + 'string'

    def test_sub(self):
        self.assertEqual(Fraction(1, 12), Fraction(3, 4) - Fraction(2, 3))
        self.assertEqual(Fraction(2, 7), Fraction(3, 7) - Fraction(1, 7))

        self.assertEqual(Fraction(1, 0), Fraction(1, 0) - Fraction(100, 7))
        self.assertEqual(Fraction(-1, 0), Fraction(-1, 0) - Fraction(100, 7))
        # inf + inf
        self.assertEqual(Fraction(-1, 0), Fraction(-1, 0) - Fraction(1, 0))
        # inf - inf -> indeterminate
        self.assertTrue((Fraction(1, 0) - Fraction(1, 0)).isnan())
        self.assertTrue((Fraction(-1, 0) - Fraction(-1, 0)).isnan())

        # other types
        self.assertEqual(Fraction(-2, 7), Fraction(5, 7) - 1)
        self.assertEqual(Fraction(51, 14), Fraction(50, 7) - 3.5)
        self.assertEqual(Fraction(-1, 0), Fraction(3, 4) - math.inf)
        self.assertTrue((Fraction(1) - math.nan).isnan())
        with self.assertRaises(TypeError):
            Fraction(3, 4) - 'string'

    def test_mul(self):
        self.assertEqual(Fraction(1, 4), Fraction(1, 3) * Fraction(3, 4))
        self.assertEqual(Fraction(-2, 21), Fraction(1, 3) * Fraction(-2, 7))

        self.assertEqual(Fraction(1, 0), Fraction(1, 0) * Fraction(1, 7))
        self.assertEqual(Fraction(-1, 0), Fraction(1, 0) * Fraction(-1, 7))
        self.assertEqual(Fraction(1, 0), Fraction(-1, 0) * Fraction(-1, 7))
        # inf x inf
        self.assertEqual(Fraction(1, 0), Fraction(1, 0) * Fraction(1, 0))
        self.assertEqual(Fraction(-1, 0), Fraction(1, 0) * Fraction(-1, 0))
        self.assertEqual(Fraction(1, 0), Fraction(-1, 0) * Fraction(-1, 0))
        # inf x 0 -> indeterminate
        self.assertTrue((Fraction(1, 0) * Fraction(0, 1)).isnan())
        self.assertTrue((Fraction(-1, 0) * Fraction(0, 1)).isnan())

        # other types
        self.assertEqual(Fraction(-5, 7), Fraction(5, 7) * -1)
        self.assertTrue((Fraction(1, 0) * 0).isnan())
        self.assertEqual(Fraction(21, 8), Fraction(3, 4) * 3.5)
        self.assertEqual(Fraction(1, 0), Fraction(3, 4) * math.inf)
        self.assertTrue((Fraction(1) * math.nan).isnan())
        with self.assertRaises(TypeError):
            Fraction(3, 4) * 'string'

    def test_truediv(self):
        self.assertEqual(Fraction(3, 4), Fraction(1, 4) / Fraction(1, 3))
        self.assertEqual(Fraction(-7, 6), Fraction(1, 3) / Fraction(-2, 7))

        self.assertEqual(Fraction(1, 0), Fraction(1, 0) / Fraction(1, 7))
        self.assertEqual(Fraction(-1, 0), Fraction(1, 0) / Fraction(-1, 7))
        self.assertEqual(Fraction(1, 0), Fraction(-1, 0) / Fraction(-1, 7))
        # inf / inf -> indeterminate
        self.assertTrue((Fraction(1, 0) / Fraction(1, 0)).isnan())
        self.assertTrue((Fraction(1, 0) / Fraction(-1, 0)).isnan())
        self.assertTrue((Fraction(-1, 0) / Fraction(-1, 0)).isnan())
        # inf / 0
        self.assertEqual(Fraction(1, 0), Fraction(1, 0) / Fraction(0, 1))
        self.assertEqual(Fraction(-1, 0), Fraction(-1, 0) / Fraction(0, 1))

        # other types
        self.assertEqual(Fraction(5, 7), Fraction(5, 7) / 1)
        self.assertTrue((Fraction(0, 1) / 0).isnan())
        self.assertEqual(Fraction(3, 10), Fraction(3, 4) / 2.5)
        self.assertEqual(Fraction(0, 1), Fraction(3, 4) / math.inf)
        self.assertTrue((Fraction(1) / math.nan).isnan())
        with self.assertRaises(TypeError):
            Fraction(3, 4) / 'string'

    def test_gt(self):
        self.assertTrue(Fraction(1, 2) > Fraction(1, 3))
        self.assertFalse(Fraction(5, 6) > Fraction(6, 7))
        self.assertFalse(Fraction(-1, 2) > Fraction(-1, 3))
        self.assertTrue(Fraction(-5, 6) > Fraction(-6, 7))
        self.assertFalse(Fraction(3, 7) > Fraction(3, 7))

    def test_lt(self):
        self.assertFalse(Fraction(1, 2) < Fraction(1, 3))
        self.assertTrue(Fraction(5, 6) < Fraction(6, 7))
        self.assertTrue(Fraction(-1, 2) < Fraction(-1, 3))
        self.assertFalse(Fraction(-5, 6) < Fraction(-6, 7))
        self.assertFalse(Fraction(3, 7) < Fraction(3, 7))

    def test_eq(self):
        f = Fraction(1, 2)
        g = Fraction(-40, -80)
        h = Fraction(10000, 20001)  # not quite 1/2
        self.assertTrue(f == g)
        self.assertTrue(f.__eq__(g))  # same thing
        self.assertFalse(f == h)
        self.assertFalse(f.__eq__(h))

        self.assertEqual(Fraction(0), Fraction(-0))
        self.assertEqual(Fraction(1, 0), Fraction(100, 0))
        self.assertEqual(Fraction(-1, 0), Fraction(-100, 0))
        self.assertNotEqual(Fraction(0), Fraction(1, 0))
        self.assertNotEqual(Fraction(-1, 0), Fraction(1, 0))
        self.assertNotEqual(Fraction(0, 0), Fraction(0, 0))

    def test_neg(self):
        self.assertEqual(Fraction(0), -Fraction(0))
        self.assertEqual(Fraction(-1, 0), -Fraction(1, 0))
        self.assertEqual(Fraction(-7, 13), -Fraction(7, 13))
        self.assertEqual(Fraction(-3, 2), -Fraction(3, 2))
        self.assertEqual(Fraction(3, 1), -Fraction(-3, 1))
        self.assertEqual(Fraction(2, 5), -Fraction(-2, 5))
        self.assertTrue(Fraction(0, 0).__neg__().isnan())

    def test_is_positive(self):
        self.assertTrue(Fraction(1).is_positive())
        self.assertFalse(Fraction(0).is_positive())
        self.assertFalse(Fraction(-1).is_positive())
        self.assertFalse(Fraction(0, 0).is_positive())

    def test_is_negative(self):
        self.assertFalse(Fraction(1).is_negative())
        self.assertFalse(Fraction(0).is_negative())
        self.assertTrue(Fraction(-1).is_negative())
        self.assertFalse(Fraction(0, 0).is_negative())

    def test_is_zero(self):
        self.assertFalse(Fraction(1).is_zero())
        self.assertTrue(Fraction(0).is_zero())
        self.assertFalse(Fraction(-1).is_zero())
        self.assertFalse(Fraction(0, 0).is_zero())

    def test_is_infinite(self):
        self.assertTrue(Fraction(1, 0).is_infinite())
        self.assertFalse(Fraction(0, 1).is_infinite())
        self.assertTrue(Fraction(-1, 0).is_infinite())
        self.assertFalse(Fraction(0).is_infinite())
        self.assertFalse(Fraction(0, 0).is_infinite())

    def test_isnan(self):
        self.assertFalse(Fraction(1, 0).isnan())
        self.assertFalse(Fraction(0, 1).isnan())
        self.assertFalse(Fraction(-1, 0).isnan())
        self.assertFalse(Fraction(0).isnan())
        self.assertTrue(Fraction(0, 0).isnan())
