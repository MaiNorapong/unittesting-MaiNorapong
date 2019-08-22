## Unit Testing Assignment

by Bill Gates.


## Test Cases for unique

| Test case              |  Expected Result    |
|------------------------|---------------------|
| empty list             |  empty list         |
| one item               |  list with 1 item   |
| one item many times    |  list with 1 item   |
| 2 items, many times, many orders | 2 item list, items in same order  |
| multiple items         |  list with all items with same order  |
| multiple items, many times  |  list with no same item  |
| list with one nested list  |  list with one nested list, nested list items unchanged  |
| list with one nested list many times  |  list with one nested list  |
| list with two nested list  |  list with two nested list with same order, nested list items unchanged  |
| list with two nested list many times  |  list with two nested list  |
| not a list             |  raise TypeError    |
| a large list           |  regular result     |

## Test Cases for Fraction

| Test case (constructor) | Expected Result    |
|------------------------|---------------------|
| zero as denominator    | one is numerator    |
| zero as numerator      | one is denominator  |
| zero as both           | raise ValueError    |
| numerator and denominator have no common factors | same number is used |
| numerator and denominator have common factors | the simplest ratio is used |
| negative numerator     | numerator is negative and denominator is positive |
| negative denominator   | numerator is negative and denominator is positive |
| negative numerator and denominator | both numerator and denominator is positive |
| floating point numbers | the simplest ratio is used |

| Test case (operations) |  Expected Result    |
|------------------------|---------------------|
| infinity and normal    |    same infinity    |
| infinity and zero      |    infinity / nan   |
| infinity and infinity    |  infinity / nan   |
| infinity and neg infinity | infinity / nan   |
| neg infinity and neg infinity | infinity / nan |
| operation result in not proper form | the simplest ratio is used |
| operation result in proper form | the simplest ratio is used |
| operation with other types | int and float supported, others not |
| operation with nan / inf | results similar to float |
