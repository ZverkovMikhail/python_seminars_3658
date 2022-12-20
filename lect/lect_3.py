# def calc(x):
#     return x**2
# #
# #
# # pow_f = f
# # print(pow_f(2))
#
#
# def math(f, x):
#     print(f(x))
#
#
# math(calc,  10)


# def sum(x, y):
#     return x + y
#
#
# def mult(x, y):
#     return x * y
#
#
# def calc(op, a, b):
#     print(op(a, b))
#
#
pow_f = lambda x: x ** 2

#
# calc(sum, 5, 4)
# calc(mult, 5, 4)
# calc(pow_f, 5, 2)
# calc(lambda q, w: q ** w, 5, 2)

# list = [(i, pow_f(i)) for i in range(1, 21) if i % 2 == 0]
# print(list)


# def select(f, col):
#     return [f(x) for x in col]
#
#
# def where(f, col):
#     return [x for x in col if f(x)]
#
#
# data = '1 2 3 5 8 15 23 38'.split(' ')
#
# res = select(int, data)
# res = where(lambda x: not x % 2, res)
# res = select(lambda x: (x, x ** 2), res)
#
# print(res)
# print(select(lambda x: (x, x ** 2), where(lambda x: not x % 2, select(int, data))))
#
# li = [x for x in range(1, 21)]
#
# li = map(lambda x:x+10, li)
# print(list(li))


print(list(map(lambda x: (x, x ** 2), filter(lambda x: not x % 2, map(int, '1 2 3 5 8 15 23 38'.split(' '))))))


print(list(zip ([1, 2, 3], [ 'о', 'д', 'т'], ['f','s','t']) ))
data = list(enumerate('1 2 3 5 8 15 23 38'.split(' ')))

print(data)