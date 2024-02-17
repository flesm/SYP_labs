class Micola():
    def __init__(self, name, age):
        if "Мікола" in name:
            self.name = name
        else:
            self.name = f"Я не {name}, а Мікола"
        self.age = age

    def __setattr__(self, name, value):
        try:
            if name not in ("name", "age"):
                raise AttributeError("Нельга дадаваць новыя ўласцівасці або метады да класу Mikola")
            super().__setattr__(name, value)
        except AttributeError as e:
            print(f"Памылка: {e}")

    def __repr__(self):
        return f"{self.__class__.__name__}({self.name}; {self.age})"


micola = Micola("Мікола", 18)
print(micola)

fake_micola = Micola("Міця", 52)
print(fake_micola)

micola.patronymic = "Аляксандравіч"
