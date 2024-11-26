def trim_and_repeat(string, offset=0, repetitions=1):
    trimmed_string = string[offset:]
    result = trimmed_string * repetitions
    return result

print(trim_and_repeat("Пример строки", 7, 3))  # Вывод: "строкистрокистроки"
print(trim_and_repeat("Пример строки"))        # Вывод: "Пример строки"
