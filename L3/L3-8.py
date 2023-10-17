import random

# 生成多组长度递增的随机整数列表
num_lists = []  # 存储多组随机数列

num_of_lists = 5  # 想要生成的随机数列的数量
min_length = 5    # 最小数列长度
max_length = 20  # 最大数列长度
max_value = 100   # 随机数的最大值

prev_length = 0   # 上一个数列的长度

for _ in range(num_of_lists):
    # 生成随机数列长度，确保长度递增
    length = random.randint(prev_length, max_length)
    prev_length = length
    
    # 生成随机数列
    random_numbers = [random.randint(1, max_value) for _ in range(length)]
    
    # 添加到列表中
    num_lists.append(random_numbers)

# 打印生成的多组随机数列
for i, numbers in enumerate(num_lists):
    print(f"Random List {i + 1}: {numbers}")

#选择排序
for i, numbers in enumerate(num_lists):
    n = len(numbers)
    for j in range(n - 1):
        min_idx = j
        for k in range(j + 1, n):
            if numbers[k] < numbers[min_idx]:
                min_idx = k
        numbers[j], numbers[min_idx] = numbers[min_idx], numbers[j]

# 打印选择排序后的多组随机数列
for i, numbers in enumerate(num_lists):
    print(f"Sorted List {i + 1}: {numbers}")

# 归并排序函数
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    return merge(left_half, right_half)

def merge(left, right):
    result = []
    left_idx, right_idx = 0, 0

    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] < right[right_idx]:
            result.append(left[left_idx])
            left_idx += 1
        else:
            result.append(right[right_idx])
            right_idx += 1

    result.extend(left[left_idx:])
    result.extend(right[right_idx:])
    return result

# 使用归并排序对每个数列进行排序
sorted_num_lists = [merge_sort(numbers) for numbers in num_lists]

# 打印排序后的多组随机数列
for i, numbers in enumerate(sorted_num_lists):
    print(f"Sorted List {i + 1}: {numbers}")

#分析两者效果：
#选择排序：对于长度较小的数列，选择排序速度较快，性能较好
#归并排序：对于长度较长的数列，归并排序速度较快，性能更好