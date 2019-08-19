from __future__ import annotations

from typing import Tuple, Union
import math


def to_proper(numerator: int, denominator: int) -> Tuple[int, int]:
    """Converts `numerator` and `denominator` to their simplest ratio.

    Examples:
        >>> to_proper(7, 28)
        (1, 4)
        >>> to_proper(-36, 54)
        (-2, 3)
        >>> to_proper(3, 4)
        (3, 4)
    """
    if numerator == 0:
        if denominator == 0:
            raise ValueError('numerator and denominator cannot be 0 at the same time')
        return 0, 1
    if denominator == 0:
        if numerator > 0:
            return 1, 0
        return -1, 0
    gcd = math.gcd(numerator, denominator)
    assert gcd > 0
    assert (numerator / gcd).is_integer()
    assert (denominator / gcd).is_integer()
    sign = numerator * denominator / abs(numerator * denominator)
    return int(sign * abs(numerator) / gcd), int(abs(denominator) / gcd)


def to_ratio(x: float) -> Tuple[int, int]:
    """Converts number to a pair of integer ratio with positive denominator.

    Examples:
        >>> to_ratio(5.6)
        (28, 5)
        >>> to_ratio(0.875)
        (7, 8)
        >>> to_ratio(-0.048)
        (-6, 125)
    """
    i = 0
    num = x
    while not num.is_integer():
        num *= 10
        i += 1
    num = int(num)
    assert x == num / 10**i
    return to_proper(num, 10**i)


class Fraction:
    """A fraction with a numerator and denominator and arithmetic operations.

    Fractions are always stored in proper form, without common factors in 
    numerator and denominator, and denominator >= 0.
    Since Fractions are stored in proper form, each value has a
    unique representation, e.g. 4/5, 24/30, and -20/-25 have the same
    internal representation.
    """

    def __init__(self, numerator, denominator=1):
        """Initialize a new fraction with the given numerator
           and denominator (default 1).
        """
        if isinstance(numerator, int) and isinstance(denominator, int):
            self.numerator, self.denominator = to_proper(numerator, denominator)
        elif isinstance(numerator, float) or isinstance(numerator, float):
            f = Fraction(*to_ratio(numerator)) / Fraction(*to_ratio(denominator))
            self.numerator, self.denominator = f.numerator, f.denominator
        else:
            raise TypeError('numerator and denominator muse be numbers')
        assert isinstance(self.numerator, int)
        assert isinstance(self.denominator, int)

    def __str__(self):
        return f"{self.numerator}{f'/{self.denominator}' if self.denominator != 1 else ''}"

    def __repr__(self):
        return self.__str__()

    def __add__(self, other: Fraction) -> Union[Fraction, math.nan]:
        """Return the sum of two fractions as a new fraction.
           Use the standard formula  a/b + c/d = (ad+bc)/(b*d)
        """
        if self.is_infinite() and other.is_infinite():
            if self.is_positive():
                if other.is_positive():
                    return Fraction(1, 0)
                return math.nan
            if other.is_negative():
                return Fraction(-1, 0)
            return math.nan
        return Fraction(self.numerator*other.denominator + other.numerator*self.denominator,
                        self.denominator * other.denominator)

    def __sub__(self, other: Fraction) -> Union[Fraction, math.nan]:
        return self + (-other)

    def __mul__(self, other: Fraction) -> Union[Fraction, math.nan]:
        try:
            return Fraction(self.numerator * other.numerator, self.denominator * other.denominator)
        except ValueError:
            return math.nan

    def __truediv__(self, other: Fraction) -> Union[Fraction, math.nan]:
        if self.denominator * other.numerator == 0:
            if self.numerator * other.denominator == 0:
                return math.nan
            if other.numerator < 0:
                return Fraction(-self.numerator * other.denominator, 0)
        return Fraction(self.numerator * other.denominator, self.denominator * other.numerator)

    def __gt__(self, other: Fraction):
        # avoids dividing because apparently multiplication is easier?
        return self.numerator * other.denominator > other.numerator * self.denominator

    def __lt__(self, other: Fraction):
        # avoids dividing because apparently multiplication is easier?
        return self.numerator * other.denominator < other.numerator * self.denominator

    def __eq__(self, other: Fraction):
        """Two fractions are equal if they have the same value.
           Fractions are stored in proper form so the internal representation
           is unique (3/6 is same as 1/2).
        """
        return self.numerator == other.numerator and self.denominator == other.denominator

    def __neg__(self):
        return Fraction(-self.numerator, self.denominator)

    def is_positive(self):
        return self.numerator > 0

    def is_negative(self):
        return self.numerator < 0

    def is_zero(self):
        return self.numerator == 0

    def is_infinite(self):
        return self.denominator == 0
