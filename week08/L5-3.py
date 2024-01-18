import seaborn as sns  
import matplotlib.pyplot as plt  
  
# 示例数据  
tips = sns.load_dataset("tips")  
  
# 绘制折线图  
plt.figure(figsize=(6, 6))  
sns.lineplot(x="total_bill", y="tip", data=tips)  
plt.title('Line Plot')  
plt.xlabel('Total Bill')  
plt.ylabel('Tip')  
plt.show()  
  
# 绘制柱状图  
plt.figure(figsize=(6, 6))  
sns.barplot(x="day", y="total_bill", data=tips)  
plt.title('Bar Chart')  
plt.xlabel('Day')  
plt.ylabel('Total Bill')  
plt.show()  
  
# 绘制散点图  
plt.figure(figsize=(6, 6))  
sns.scatterplot(x="total_bill", y="tip", data=tips)  
plt.title('Scatter Plot')  
plt.xlabel('Total Bill')  
plt.ylabel('Tip')  
plt.show()