from wordcloud import WordCloud
import csv
import imageio.v2 as imageio

file = open('C:/大学/竞赛/全民数字素养与人工智能创新应用大赛/b站爬虫/最佳旅拍的弹幕.csv','r',encoding = 'utf-8')
lst =[]

for line in file.readlines():  
    content = line.split(',')
    lst.append(content[0])

txt = str(lst)

img = imageio.imread('xyc.jpg')

wc = WordCloud(width = 10000, height =10000, 
               background_color = 'white', 
               font_path = 'C:\Windows\Fonts\msyh',
               mask = img)
wc.generate(txt)

wc.to_file('haha.png')