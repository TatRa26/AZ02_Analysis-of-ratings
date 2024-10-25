import pandas as pd
import numpy as np

# Создаем данные для учеников грузинской школы
data = {
    'Имя': [
        'Анна', 'Бека', 'Гиорги', 'Давид', 'Элене',
        'Иракли', 'Катя', 'Леван', 'Нино', 'Тамта'
    ],
    'Математика': [85, 76, 90, 88, 92, 78, 84, 69, 95, 82],
    'Грузинский язык': [89, 78, 92, 85, 94, 80, 88, 75, 91, 84],
    'История': [78, 85, 80, 92, 86, 81, 83, 88, 90, 87],
    'Физика': [75, 88, 91, 85, 90, 79, 87, 83, 92, 80],
    'Химия': [80, 82, 88, 91, 85, 87, 83, 79, 90, 84]
}

# Создаем DataFrame
df = pd.DataFrame(data)

# Сохраняем DataFrame в CSV-файл
csv_file_path = 'georgian_school_grades.csv'
df.to_csv(csv_file_path, index=False)

# Вывод первых строк DataFrame для проверки
print("Первые строки DataFrame:")
print(df.head())

# Средняя оценка по каждому предмету
mean_grades = df.mean(numeric_only=True)
print("\nСредняя оценка по каждому предмету:")
print(mean_grades)

# Медианная оценка по каждому предмету
median_grades = df.median(numeric_only=True)
print("\nМедианная оценка по каждому предмету:")
print(median_grades)

# Q1 и Q3 для оценок по математике
Q1_math = df['Математика'].quantile(0.25)
Q3_math = df['Математика'].quantile(0.75)
IQR_math = Q3_math - Q1_math

print("\nQ1 и Q3 для оценок по математике:")
print(f"Q1 (первый квартиль): {Q1_math}")
print(f"Q3 (третий квартиль): {Q3_math}")
print(f"IQR (интерквартильный размах): {IQR_math}")

# Стандартное отклонение по каждому предмету
std_dev = df.std(numeric_only=True)
print("\nСтандартное отклонение по каждому предмету:")
print(std_dev)
