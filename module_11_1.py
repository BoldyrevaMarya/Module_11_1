import numpy as np

# Создание одномерного массива
array_1d = np.array([1, 2, 3, 4, 5])
print("Одномерный массив:", array_1d)

# Выполнение арифметических операций
array_squared = array_1d ** 2
print("Квадраты элементов массива:", array_squared)

# Создание двумерного массива и вычисление суммы по столбцам
array_2d = np.array([[1, 2, 3], [4, 5, 6]])
sum_columns = np.sum(array_2d, axis=0)
print("Сумма по столбцам:", sum_columns)

import matplotlib.pyplot as plt

# Данные
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

# Создание линейного графика
plt.plot(x, y, marker='o')
plt.title('Пример линейного графика')
plt.xlabel('x')
plt.ylabel('y')
plt.grid()

# Сохранение графика
plt.savefig('line_plot.png')
plt.show()

from PIL import Image, ImageFilter

# Открытие изображения
try:
    image = Image.open('example.jpg')

    # Изменение размера изображения
    resized_image = image.resize((200, 200))
    resized_image.save('resized_image.jpg')

    # Применение размытия к изображению
    blurred_image = image.filter(ImageFilter.BLUR)
    blurred_image.save('blurred_image.jpg')

    print("Изображения успешно обработаны и сохранены.")
except FileNotFoundError:
    print("Ошибка: файл 'example.jpg' не найден. Пожалуйста, убедитесь, что файл существует в текущей директории.")
except Exception as e:
    print("Произошла ошибка:", e)