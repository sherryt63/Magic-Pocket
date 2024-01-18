def insertion_sort(arr):  
    for i in range(1, len(arr)):  
        key = arr[i]  
        j = i - 1  
        while j >= 0 and key < arr[j]:  
            arr[j + 1] = arr[j]  
            j -= 1  
        arr[j + 1] = key  
    return arr

#流程图：
'''
开始  
    |  
输入数据：n个元素  
    |  
for i = 1 to n-1 do  
    |  
    |-- 当前元素存储在变量key中 --|  
    |  
    |-- 将变量j设置为当前元素的前一个元素的索引 --|  
    |  
    |-- 如果当前元素小于前一个元素，将前一个元素向右移动一位，并将j减少1 --|  
    |  
    v  
将key插入到正确的位置中  
    |  
end for  
    |  
输出排序后的数据  
    |  
结束
'''