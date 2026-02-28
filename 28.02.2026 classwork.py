import time

import numpy as np
# # arr = np.array([-6,4,9,12,7,3])
# #
# # arr_condition = arr % 3 == 0
# # print(arr_condition)
# #
# # arr1 = arr[arr % 3 == 0]
# # print(arr1)
# #
# # np.sum(arr % 3 == 0)
# # np.sum(arr[arr % 3 == 0])
#
# arr = np.array([0,1,2,3,4,5,6,7,8,9,-3])
# # в numpy только амперсанта &
# arr_condition = (arr > 3) & (arr < 8)
# print(np.sum(arr_condition))
# print(np.sum(arr[arr_condition]))
# print(arr[arr_condition])
#
# mean_value = np.mean(arr)
# print(mean_value)
#
# arr_condition_2 = (arr % 2 == 0) > 2
# print(np.sum(arr_condition_2))
#
# count_condition = arr <= 8
# print(np.sum(count_condition))

arr = np.arange(-5,30)
# print(arr)
#
# arr_condition = arr % 7 == 0
# print(arr_condition)
#
# max_number = np.max(arr[arr_condition])
# print(max_number)

# count_condition = arr % 3 != 0
# print(count_condition)
# print(np.sum(count_condition))

# condition_2 = (arr > 20) | (arr < 30)
# print(np.sum(arr[condition_2]))

# замер замер вычитание старта из конца


arr_np = np.arange(1_000_001)
# start
time_start = time.perf_counter()
arr_np_condition = arr_np >= 60
print(np.sum(arr_np_condition))
time_end = time.perf_counter()
# end
# разница генерацию не учитываем только время работы функции
print(time_end - time_start)
count = 0
arr_python = list(range(1_000_001))
time_start = time.perf_counter()
for element in arr_python:
    if element >= 60:
        count += 1
time_end = time.perf_counter()
print(count)
print(time_end - time_start)
