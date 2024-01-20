import requests
import xml.etree.ElementTree as ET
import pandas as pd


#获取弹幕
def get_bilibili_danmaku(cid):   
    url = f"https://comment.bilibili.com/{cid}.xml"    #f前缀代表格式化字符串，里面可以包含{cid}这种占位符，使其之后能被替换
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.content
    else:
        print(f"Error accessing the API. Status Code: {response.status_code}")
    return None


#解析弹幕
def parse_danmaku(xml_content):
    root = ET.fromstring(xml_content)    #解析xml格式的字符串
    danmaku_list = []

    for d in root.iter('d'):    #遍历xml树中所有标签为'd'的元素
        danmaku_text = d.text   
        danmaku_attr = d.attrib #返回d的属性字典
        time_info = danmaku_attr.get('p', '').split(',')
        
        if len(time_info) > 0:
            video_time = int(float(time_info[0]))  # #弹幕在视频中的出现时间（秒），转为整数秒
            hours = video_time // 3600
            minutes = (video_time % 3600) // 60
            seconds = video_time % 60
            real_time = f"{hours}:{minutes}:{seconds}"  # 格式化时间，取整到小时、分钟、秒'''

            date = time_info[4]
            
            danmaku_list.append({
                '弹幕': danmaku_text,
                '视频中时间': video_time,
                '发送时间戳': date
            })
    return danmaku_list


#将获取的弹幕信息保存到excel中
def save_danmaku_to_excel(danmaku_list, filename):    
    df = pd.DataFrame(danmaku_list)
    df.to_excel(filename, index=False, engine='openpyxl')
    print(f"保存了 {len(danmaku_list)} 条弹幕到 {filename}")



if __name__ == '__main__':
    cid = input('输入视频的cid:')
    danmaku_xml = get_bilibili_danmaku(cid) 

    if danmaku_xml:
        danmaku_list = parse_danmaku(danmaku_xml)
        filename = f"{cid}的弹幕.xlsx"
        save_danmaku_to_excel(danmaku_list, filename)
    else:
        print("无法获取弹幕。")
