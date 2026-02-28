#1 Создайте одномерный массив из чисел от 1 до 10 с помощью np.array().
# import numpy as np
# arr1 = np.array([1,2,3,4,5,6,7,8,9,10])

#2 Создайте массив из 7 элементов, заполненных нулями.
# import numpy as np
# arr_zeros = np.zeros(7)

#3 Создайте массив из 5 единиц.
# import numpy as np
# arr_ones = np.ones(5)

#4 Создайте массив от 10 до 50 с шагом 5.
# import numpy as np
# arr_range = np.arange(10,50,5)

#5 Создайте массив из 6 чисел, равномерно распределенных от 0 до 100.
# import numpy as np
# arr_linspace = np.linspace(0,100)
# print(arr_linspace)

#6 Создайте массив и выведите второй элемент, последний элемент и
# элементы с индексами от 3 до 6.
# import numpy as np
# arr_range = np.arange(1,21)
# print(arr_range[1])
# print(arr_range[-1])
# print(arr_range[3],arr_range[6])

#7 Создайте одномерный массив и выведите его элементы с помощью цикла
# import numpy as np
# arr1 = np.array([1,2,3,4,5,6,7,8])
# for element in arr1:
#     print(element)

#8	Создайте два массива одинаковой длины и сложите их поэлементно.
# import numpy as np
# arr1 = np.arange(1,21)
# arr2 = np.arange(1,21)
# arr_sum = arr1 + arr2
# print(arr_sum)

#9	Создайте массив и умножьте все его элементы на 2.
# import numpy as np
# arr1 = np.arange(1,20)
# arr2 = arr1 * 2
# print(arr2)

#10	Создайте массив и возведите все его элементы в квадрат.
# import numpy as np
# arr = np.arange(1,10)
# arr_square = arr ** 2
# print(arr_square)

#11	Создайте массив и найдите его минимум и максимум с использованием функций np.min() и np.max().
# import numpy as np
# arr = np.arange(1,15)
# arr_mini = np.min(arr)
# arr_maxi = np.max(arr)
# print(arr_mini, arr_maxi)

#12	Создайте массив и вычислите его среднее значение и стандартное отклонение.
# import numpy as np
# arr = np.arange(1,20)
# arr_mean = np.mean(arr)
# arr_std = np.std(arr)
# print(arr_mean)
# print(arr_std)
#13 Примените к элементам массива функции np.log(), np.exp() и np.sin().
# import numpy as np
# arr = np.arange(1,31)
# arr_log = np.log(arr)
# arr_exp = np.exp(arr)
# arr_sin = np.sin(arr)

#14	Создайте массив из 10 случайных чисел, распределенных от 0 до 1.
# import numpy as np
# arr_random = np.random.randint(0,2,size = 10)
# print(arr_random)

#15	Создайте массив из 6 случайных целых чисел от 1 до 100.
# import numpy as np
# arr_random = np.random.randint(1,100,size = 6)

#16	Преобразуйте одномерный массив в двумерный массив с 2 строками и 5 столбцами
import numpy as np
arr = np.arange(1,6)
arr_matrix = arr.reshape(2,5)
print(arr)
print(arr_matrix)
#17 Измените форму одномерного массива с 9 элементами на двумерный массив 3x3.
#18 Создайте массив и выберите только те элементы, которые больше 5.
#19 Создайте массив и примените функцию возведения в куб ко всем его элементам с помощью np.vectorize().
#20 Сохраните одномерный массив в файл .npy и загрузите его обратно в программу.
