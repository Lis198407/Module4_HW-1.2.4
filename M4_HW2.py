# Module 4
# HW 2
"""
Вимоги до завдання:
Функція get_cats_info(path) має приймати один аргумент - шлях до текстового файлу (path).
Файл містить дані про котів, де кожен запис містить унікальний ідентифікатор, ім'я кота та його вік.
Функція має повертати список словників, де кожен словник містить інформацію про одного кота.


Рекомендації для виконання:
Використовуйте with для безпечного читання файлу.
Пам'ятайте про встановлення кодування при відкриті файлів
Для кожного рядка в файлі використовуйте split(',') для отримання ідентифікатора, імені та віку кота.
Утворіть словник з ключами "id", "name", "age" для кожного кота та додайте його до списку, який буде повернуто.
Опрацьовуйте можливі винятки, пов'язані з читанням файлу.
"""

from pathlib import Path

def  get_cats_info(file_path: Path):
    try:
        cat_dict= {}
        cats_list=[]
        with open(file_path, "r", encoding="utf-8") as file:
            for line in file:
                try:
                    line = line.strip()
                    cat_str = line.split(",")
                    cat_dict = {
                        'id': cat_str[0],
                        'name': cat_str[1],
                        'age': float(cat_str[2])
                        }
                    cats_list.append(cat_dict)
                except Exception as ex:
                    print(f"mistake in data structure: {ex}, line: {line}")
      
    except FileNotFoundError as ex:
        print(f"{ex}")
    
    return cats_list

def main():
    file_path = Path("cats.txt")
    cats_info = get_cats_info(file_path)
    print(cats_info)

if __name__ == "__main__":
    main()
