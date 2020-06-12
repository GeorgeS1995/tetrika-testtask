'''
Дан массив целых чисел array и целое число k. Нужно вывести все уникальные пары чисел из массива, сумма которых равна k.

Примечание: под уникальностью понимается следующее: если ответу удовлетворяет несколько пар вида (a, b) и (b, a), то достаточно вывести только одну пару (a, b).
'''


def search_pairs(array, k):
    res = []
    used_numbers = set()
    for start_index in range(len(array)):
        if array[start_index] in used_numbers:
            continue
        for compaired in array[start_index + 1:]:
            if compaired in used_numbers:
                continue
            if compaired + array[start_index] == k:
                res.append((array[start_index], compaired))
                used_numbers.add(array[start_index])
                used_numbers.add(compaired)
    return res


assert search_pairs([1, 2, 6, 5, 3, 4, 7, 8, 3, 2], 5) == [(1, 4), (2, 3)]
