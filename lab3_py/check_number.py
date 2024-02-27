import PySimpleGUI as sg


def true_checker(tf):
    if tf:
        return "з'яўляецца"
    else:
        return "не з'яўляецца"


class NumberClassifier:
    def __init__(self, number):
        self.number = number

    def is_prime(self):
        if self.number < 2:
            return False
        for i in range(2, int(self.number ** 0.5) + 1):
            if self.number % i == 0:
                return False
        return True

    def is_fibonacci(self):
        a, b = 0, 1
        while a < self.number:
            a, b = b, a + b
        return a == self.number

    def is_complex(self):
        return isinstance(self.number, complex)

    def is_integer(self):
        return isinstance(self.number, int)

    def is_real(self):
        return isinstance(self.number, float) or isinstance(self.number, int)


layout = [
    [sg.Text("Увядзіце лік:"), sg.InputText(key="number")],
    [sg.Button("Выканаць аналіз")]
]

window = sg.Window("Аналіз лікаў", layout)

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

    try:
        number = int(values["number"])
        num = NumberClassifier(number)
        prime_result = true_checker(num.is_prime())
        fibonacci_result = true_checker(num.is_fibonacci())
        complex_result = true_checker(num.is_complex())
        integer_result = true_checker(num.is_integer())
        real_result = true_checker(num.is_real())

        sg.popup(f"Лік {num.number} {prime_result} простым.",
                 f"Лік {num.number} {fibonacci_result} лікам Фібаначы.",
                 f"Лік {num.number} {complex_result} камплексным.",
                 f"Лік {num.number} {integer_result} цэлым.",
                 f"Лік {num.number} {real_result} рэчаісным.")

    except ValueError:
        sg.popup("Некарэктны ўвод. Паспрабуйце яшчэ раз.")

window.close()
