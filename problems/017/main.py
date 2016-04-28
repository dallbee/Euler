"""
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?


NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.
"""

singles = [
    '', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine'
]

teens = [
    'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen'
]

tens = [
    '', '', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety'
]

def number(i):
    if i < 10:
        return singles[i] 
    if i < 20:
        return teens[i % 10]
    if i < 100:
        return tens[i // 10] + singles[i % 10]
    if i == 1000:
        return 'onethousand'
    if i % 100 == 0:
        return singles[i // 100] + 'hundred'
    return singles[i // 100] + 'hundredand' + number(i % 100)


print(sum([len(number(i)) for i in range(1, 1001)]))
