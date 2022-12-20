import re

math = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '*': lambda x, y: x * y,
    '^': lambda x, y: x ** y,
    '/': lambda x, y: x / y,
}


def calc(text):
    try:
        mask = '[\u005C' + '\u005C'.join([s for s in math.keys()]) + ']'
        sign = re.findall(mask, text)[0]
        nums = list(map(int, re.findall(r'(\d+)', text)))
    except IndexError:
        return None
    return math[sign](nums[0], nums[1])
