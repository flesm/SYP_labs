import pickle

rad = input("Увядзіце лікі праз прабел: ")

lst = []
for x in rad.split():
    try:
        lst.append(int(x))
    except ValueError:
        pass
tpl = tuple(lst)

with open("tuple.bin", "ab") as f:
    pickle.dump(tpl, f)
    print(f"Картэж {tpl} запісаны ў файл.")

