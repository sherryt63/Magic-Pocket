import time  
  
def my_function():  
    # 执行一些操作  
    pass  
  
start_time = time.time()  
my_function()  
end_time = time.time()  
  
elapsed_time = end_time - start_time  
print("函数执行时间：", elapsed_time, "秒")