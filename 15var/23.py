def f(a, b): # Обычно ручками решаю, через граф, но сейчас какой-то жёсткий вариант ваще
    if a == b:
        return 1
    if a > b:
        return 0
    return f(a + 1, b) + f(a + 2, b) + f(a + 4, b)

print(f(21, 30))
