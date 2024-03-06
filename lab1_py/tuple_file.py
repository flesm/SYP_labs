import pickle

rad = input("Увядзіце лікі праз прабел: ")

lst = []
for x in rad.split():
    try:

        # ствараем спіс лікаў
        lst.append(int(x))
    except ValueError:
        pass
tpl = tuple(lst)

with open("tuple.bin", "ab") as f:

    # серэалізуем картэж і запісваем ў файл
    pickle.dump(tpl, f)
    print(f"Картэж {tpl} запісаны ў файл.")

