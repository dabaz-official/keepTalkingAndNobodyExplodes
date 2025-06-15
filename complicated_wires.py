def solve(bomb_info):
    print("\n=== 复杂线路 ===")

    # 询问电线数量
    while True:
        try:
            num_wires = int(input("请输入电线数量（正整数）："))
            if num_wires > 0:
                break
            print("电线数量必须为正整数！")
        except ValueError:
            print("请输入有效的数字！")

    # 获取炸弹信息
    last_digit_odd = bomb_info["last_digit_odd"]
    battery_count = bomb_info["battery_count"]
    has_parallel = bomb_info["has_parallel_port"]

    # 存储每根电线的剪断指令
    results = []

    # 循环处理每根电线
    for wire_num in range(1, num_wires + 1):
        print(f"\n处理第 {wire_num} 根电线：")
        # 获取 4 种情况
        while True:
            has_red = input("线路有红色？（y/n）：").strip().lower()
            if has_red in ['y', 'n']:
                has_red = has_red == 'y'
                break
            print("请输入 y 或 n！")

        while True:
            has_blue = input("线路有蓝色？（y/n）：").strip().lower()
            if has_blue in ['y', 'n']:
                has_blue = has_blue == 'y'
                break
            print("请输入 y 或 n！")

        while True:
            has_star = input("带有⭐标记？（y/n）：").strip().lower()
            if has_star in ['y', 'n']:
                has_star = has_star == 'y'
                break
            print("请输入 y 或 n！")

        while True:
            has_led = input("LED点亮？（y/n）：").strip().lower()
            if has_led in ['y', 'n']:
                has_led = has_led == 'y'
                break
            print("请输入 y 或 n！")

        # 规则 1：剪断 (C)
        if (not has_red and not has_blue and not has_star and not has_led) or \
                has_star or \
                (has_red and has_star):
            results.append(f"第 {wire_num} 根：剪断")
            continue

        # 规则 2：不剪断 (D)
        if (has_blue and has_star) or \
                (has_red and has_blue and has_star and has_led) or \
                has_led:
            results.append(f"第 {wire_num} 根：不剪断")
            continue

        # 规则 3：序列号末位为偶数则剪断 (S)
        if has_red or \
                (has_red and has_blue) or \
                has_blue or \
                (has_red and has_blue and has_led):
            if not last_digit_odd:  # 末位为偶数
                results.append(f"第 {wire_num} 根：剪断")
            else:
                results.append(f"第 {wire_num} 根：不剪断")
            continue

        # 规则 4：有 Parallel 端口则剪断 (P)
        if (has_red and has_blue and has_star) or \
                (has_blue and has_star and has_led) or \
                (has_blue and has_led):
            if has_parallel:
                results.append(f"第 {wire_num} 根：剪断")
            else:
                results.append(f"第 {wire_num} 根：不剪断")
            continue

        # 规则 5：有两个或更多电池则剪断 (B)
        if (has_star and has_led) or \
                (has_red and has_star and has_led) or \
                (has_red and has_led):
            if battery_count >= 2:
                results.append(f"第 {wire_num} 根：剪断")
            else:
                results.append(f"第 {wire_num} 根：不剪断")
            continue

        # 默认情况（无匹配规则）
        results.append(f"第 {wire_num} 根：不剪断")

    # 返回所有电线的剪断指令
    return "\n".join(results) if results else "无剪断指令"