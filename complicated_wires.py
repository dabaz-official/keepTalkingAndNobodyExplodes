def solve(params):
    serial_info, battery_count = params  # 解包参数
    _, _, is_last_digit_odd = serial_info  # 解包序列号信息，获取末位奇偶性

    print("\n=== 复杂线路模块 ===")

    # 询问是否有 Parallel 端口
    has_parallel = input("是否有 Parallel 端口？（y/n）：").strip().lower() == 'y'

    # 获取 4 种情况
    has_red = input("线路有红色？（y/n）：").strip().lower() == 'y'
    has_blue = input("线路有蓝色？（y/n）：").strip().lower() == 'y'
    has_star = input("带有⭐标记？（y/n）：").strip().lower() == 'y'
    has_led = input("LED点亮？（y/n）：").strip().lower() == 'y'

    # 规则 1：剪断 (C)
    if (not has_red and not has_blue and not has_star and not has_led) or \
            has_star or \
            (has_red and has_star):
        return "剪断"

    # 规则 2：不剪断 (D)
    if (has_blue and has_star) or \
            (has_red and has_blue and has_star and has_led) or \
            has_led:
        return "不剪断"

    # 规则 3：序列号末位为偶数则剪断 (S)
    if has_red or \
            (has_red and has_blue) or \
            has_blue or \
            (has_red and has_blue and has_led):
        if not is_last_digit_odd:  # 末位为偶数
            return "剪断"
        return "不剪断"

    # 规则 4：有 Parallel 端口则剪断 (P)
    if (has_red and has_blue and has_star) or \
            (has_blue and has_star and has_led) or \
            (has_blue and has_led):
        if has_parallel:
            return "剪断"
        return "不剪断"

    # 规则 5：有两个或更多电池则剪断 (B)
    if (has_star and has_led) or \
            (has_red and has_star and has_led) or \
            (has_red and has_led):
        if battery_count >= 2:
            return "剪断"
        return "不剪断"

    # 默认情况（无匹配规则）
    return "不剪断"