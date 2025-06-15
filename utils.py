def get_serial_info():
    while True:
        serial = input("请输入炸弹序列号（例如 X7Y9Z1）：").strip().upper()
        if serial:
            # 计算奇数位数字总数
            odd_count = sum(1 for char in serial if char.isdigit() and int(char) % 2 == 1)
            # 判断末位数字奇偶性
            last_digit = next((char for char in serial[::-1] if char.isdigit()), None)
            last_digit_odd = int(last_digit) % 2 == 1 if last_digit else False
            # 判断是否有元音字母
            has_vowel = any(char in 'AEIOU' for char in serial)
            return {
                "serial": serial,
                "odd_digits_count": odd_count,
                "last_digit_odd": last_digit_odd,
                "has_vowel": has_vowel
            }
        print("序列号不能为空，请重新输入。")

def get_battery_count():
    while True:
        try:
            count = int(input("请输入电池数量（0 或正整数）："))
            if count >= 0:
                return count
            print("电池数量不能为负数！")
        except ValueError:
            print("请输入有效的数字！")

def get_parallel_port():
    while True:
        response = input("炸弹是否有并行端口（parallel port）？(y/n)：").strip().lower()
        if response in ['y', 'n']:
            return response == 'y'
        print("请输入 'y' 或 'n'！")

def get_bomb_info():
    serial_info = get_serial_info()
    battery_count = get_battery_count()
    has_parallel_port = get_parallel_port()
    return {
        "serial": serial_info["serial"],
        "odd_digits_count": serial_info["odd_digits_count"],
        "last_digit_odd": serial_info["last_digit_odd"],
        "has_vowel": serial_info["has_vowel"],
        "battery_count": battery_count,
        "has_parallel_port": has_parallel_port
    }