import numpy as np
# задание 1
arr1 = np.random.randint(1,101,1_000_000)
arr_mean = np.mean(arr1)

condition = arr1 > 50
print(f'количество чисел больше 50: {np.sum(condition)}')

even_number_condition = arr1 % 2 == 0
print(f'количество четных чисел: {np.sum(even_number_condition)}')

odd_number_condition = arr1 % 2 != 0
print(f'количество нечетных чисел: {np.sum(odd_number_condition)}')

checking = np.sum(even_number_condition) + np.sum(odd_number_condition)
if checking == 1_000_000:
    print(f'сумма четных и нечетных {checking}')

# пробую использовать фильтр
arr2 = np.array([1,2,3,4,5,6,7])
print(np.max(arr2[arr2 % 2 == 0]))



