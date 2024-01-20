from snownlp import SnowNLP
import matplotlib.pyplot as plt    #导入画图的库(pyplot是子库)

file = open('沙雕二创 非标题党.csv', encoding = 'utf-8')
text = []
for line in file.readlines():      #依次读入弹幕文件的每一行
    content = line.split(',')
    text.append(content[0])


emotions = {'positive':0,
            'negative':0,
            'neutral':0}


for item in text:
    s = SnowNLP(item)
    if s.sentiments > 0.6:
        emotions['positive'] += 1
    elif s.sentiments < 0.4:
        emotions['negative'] += 1
    else:
        emotions['neutral'] += 1
    #print(item)

plt.style.use('fivethirtyeight')

plt.pie(emotions.values(), labels = emotions.keys(), autopct = '%1.1f%%')

plt.tight_layout()

#设置字体，显示为中文（否则会出现乱码）
plt.rcParams['font.family'] = ['sans-serif']
plt.rcParams['font.sans-serif'] = ['SimHei']

plt.title("弹幕情感分析饼图")          #添加标题
plt.savefig("弹幕情感分析饼图.jpg")    #保存图片
plt.show()                           #运行时显示


