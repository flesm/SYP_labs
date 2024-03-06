import pickle
import os


# функцыя для знаходжання мінімальнага станоўчага ліку
def min_positive(tpl):
    min_value = None
    for x in tpl:
        if x > 0:
            if min_value is None or x < min_value:
                min_value = x
    return min_value


# зчытвваем спіс усіх картэжаў з бінарнага файла
with open('tuple.bin', 'rb') as f:
    tuples = []
    while True:
        try:
            tpl = pickle.load(f)
            tuples.append(tpl)
        except EOFError:
            break

# ачыстка файла перад запісам
os.remove('result.txt')

for tup in tuples:
    result = min_positive(tup)

    with open('result.txt', 'a', encoding='UTF-8') as f:
        f.write(f"Мінімальны станоўчы лік у картэжы {tup}: {str(result)}\n")

print(f"Картэж {tuples[-1]} запісаны тэкставы файл.")
