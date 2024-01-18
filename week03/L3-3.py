import re

def validate_id_card(id_card):
    # 定义身份证号的正则表达式模式
    pattern =r'^[0-9]{6}(19|20)\d{2}((0[1-9])|(1[0-2]))(([0-2][1-9])|(3[0-1]))\d{3}(\d|X)$'
    
    # 使用re.match()函数匹配正则表达式
    if re.match(pattern, id_card):
        return True
    else:
        return False

# 测试函数
id_card = "310105200406031226"
if validate_id_card(id_card):
    print(f"{id_card} 是合法的身份证号码。")
else:
    print(f"{id_card} 不是合法的身份证号码。")
