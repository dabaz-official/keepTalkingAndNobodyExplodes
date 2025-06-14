def get_serial_number():
    while True:
        serial = input("请输入炸弹序列号（例如 X7Y9Z1）：").strip().upper()
        if serial and any(char.isdigit() for char in serial):
            # 检查是否有元音字母 (A, E, I, O, U)
            has_vowel = any(char in 'AEIOU' for char in serial)
            # 获取末位数字并判断奇偶性
            last_digit = next(char for char in reversed(serial) if char.isdigit())
            is_last_digit_odd = int(last_digit) % 2 == 1
            return serial, has_vowel, is_last_digit_odd
        print("序列号必须包含至少一个数字，请重新输入。")