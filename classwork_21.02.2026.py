# from encodings import search_function
# from idlelib.run import StdioFile
#
# import numpy as np
# import time as t
# low_N = - 500_00000
# upper_N = 500_00000
#
# arr_np = np.arange(low_N,upper_N)
# print(arr_np)
#
# arr_sum_all = np.sum(arr_np[arr_np > 0])
# print(arr_sum_all)
#
# arr_condition = arr_np % 2 == 0
# print(np.sum(arr_condition))
# # arr_condition возвращает тру ор фолз
# # мне надо подсчитать трушные значения
# # и для этого я использую sum он подсчитает трушные значения
#
#
# # arr1 = np.array([1,2,3,4,5])
# #
# # arr_condition = arr1 % 2 == 0 # кондиция = условие
# # # если кондиция то тру если не кондиция то фолз
# # print(arr_condition)
# # print(np.sum(arr_condition))
#
# arr_mean_all = np.mean(arr_np[arr_np < 0])
# print(arr_mean_all)
# arr_max_all = np.max(arr_np[arr_np % 7 == 0])
# print(arr_max_all)
#
# arr_list = list(range(low_N, upper_N))
# list_sum = sum(arr_list)
# print(list_sum)
#
# time_start = t.perf_counter()
# arr_sum_all = np.sum(arr_np)
# time_end = t.perf_counter()
# print(f'{time_end - time_start:.8f}')
#
# arr_list = list(range(low_N, upper_N))
# time_start = t.perf_counter()
# list_sum = sum(arr_list)
# time_end = t.perf_counter()
# print(f'{time_end - time_start:.8f}')
#

import numpy as np
import time as t

low_N = -50000
upper_N = 50000

arr_np = np.arange(low_N, upper_N)
arr_list = list(range(low_N, upper_N))

arr_mult = arr_np * 2
arr_mult_list = arr
time_start = t.perf_counter()

