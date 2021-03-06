'''
Написать функцию, которая возвращает количество идущих подряд нулей на конце n!.
'''


'''
Сразу скажу решение знал.
Объяснение решения: Ответ n! можно представить как f * (2 * 5).... где множители 2*5 это по сути нули в конце
Так как в факториале всегда больше четных множителей, чем которые деляться на 5, то важно понять сколько раз можно
разделить n! на 5 без остатка
'''

def get_zeros(n):
    zeros = 0
    while n >= 5:
        n //= 5
        zeros += n
    return zeros


assert get_zeros(5) == 1
assert get_zeros(12) == 2
assert get_zeros(30) == 7
assert get_zeros(100) == 24
