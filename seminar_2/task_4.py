# 4.	Напишите программу, которая проверяет пятизначное число на палиндром.


first_num = 123211
second_num = 1231321


def is_palindrome(num):
    digs = str(num)
    digs_len = len(digs)
    for i in range(digs_len // 2):
        if not digs[i] == digs[digs_len - 1 - i]:
            return False
    return True


def print_answer(num):
    print(f'{num} -> ' + ('Палиндром!' if is_palindrome(num) else 'Не палиндром!'))


print_answer(first_num)
print_answer(second_num)

