import matplotlib.pyplot as plt  
import numpy as np  
  
# 示例数据  
x = np.array([0, 1, 2, 3, 4, 5])  
y = np.array([0, 1, 4, 9, 16, 25])  
  
# 绘制线图  
plt.plot(x, y)  
plt.title('Line Plot')  
plt.xlabel('X-axis')  
plt.ylabel('Y-axis')  
plt.show()  
  
# 绘制柱状图  
plt.bar(x, y)  
plt.title('Bar Chart')  
plt.xlabel('X-axis')  
plt.ylabel('Y-axis')  
plt.show()  
  
# 绘制散点图  
plt.scatter(x, y)  
plt.title('Scatter Plot')  
plt.xlabel('X-axis')  
plt.ylabel('Y-axis')  
plt.show()