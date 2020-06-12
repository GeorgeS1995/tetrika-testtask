
file = 'names.txt'

with open(file, 'r') as f:
    words = f.read()

res = 0
words = words.replace('"', '').split(",")
words.sort()
for index, word in enumerate(words, 1):
    words_sum = 0
    for letter in word:
        words_sum += ord(letter) - ord('A') + 1
    res += words_sum * index

print(f'Сумма для всех слов: {res}')
