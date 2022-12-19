# 6.	Дан текст: в первой строке задано число строк, далее идут сами строки. Выведите слово,
# которое в этом тексте встречается чаще всего. Если таких слов несколько, выведите то,
# которое меньше в лексикографическом порядке.
# Входные данные	                    Выходные данные
# 1
# apple orange banana banana orange	    banana


input_str = 'apple orange banana banana orange'
counts = {}

for w in input_str.split(' '):
    counts[w] = counts.get(w, 0) + 1

counts = dict(sorted(counts.items()))
print(max(counts, key=counts.get))
