import json

# Решение задачи
def calculate_total() -> float:
    # Открываем входной файл с данными
    with open("input.json", "r") as input_file:
        items = json.load(input_file)  # Загружаем JSON данные

    total_weighted_score = 0  # Сумма взвешенных значений

    # Перебираем элементы и вычисляем взвешенную сумму
    for entry in items:
        total_weighted_score += entry["score"] * entry["weight"]

    # Возвращаем результат с округлением до 3 знаков
    return round(total_weighted_score, 3)


# Вывод результата
print(calculate_total())

