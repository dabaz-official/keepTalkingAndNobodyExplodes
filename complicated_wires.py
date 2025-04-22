def determine_letter():
    # 询问用户四个问题
    has_red = input("是否有红色？(y/n): ").lower() == 'y'
    has_blue = input("是否有蓝色？(y/n): ").lower() == 'y'
    has_led = input("LED 灯是否点亮？(y/n): ").lower() == 'y'
    has_star = input("是否有五角星符号？(y/n): ").lower() == 'y'

    # 构造组合字符串
    combination = ""
    if has_red:
        combination += "1"
    if has_blue:
        combination += "2"
    if has_led:
        combination += "3"
    if has_star:
        combination += "4"

    # 如果没有条件
    if not combination:
        return "推断出的字母是: C"

    # 匹配组合并返回结果
    if combination == "1234":
        return "推断出的字母是: D"
    elif combination == "123":
        return "推断出的字母是: S"
    elif combination == "234":
        return "推断出的字母是: P"
    elif combination == "124":
        return "推断出的字母是: P"
    elif combination == "134":
        return "推断出的字母是: B"
    elif combination == "12":
        return "推断出的字母是: S"
    elif combination == "23":
        return "推断出的字母是: P"
    elif combination == "34":
        return "推断出的字母是: B"
    elif combination == "13":
        return "推断出的字母是: B"
    elif combination == "24":
        return "推断出的字母是: D"
    elif combination == "1":
        return "推断出的字母是: S"
    elif combination == "2":
        return "推断出的字母是: S"
    elif combination == "3":
        return "推断出的字母是: D"
    elif combination == "4":
        return "推断出的字母是: C"
    else:
        return "无法确定字母，可能输入有误。"

# 运行程序
result = determine_letter()
print(result)