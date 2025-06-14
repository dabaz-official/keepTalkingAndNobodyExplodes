def solve(params):
    _, _ = params  # 解包参数，暂不使用 serial_info 和 battery_count

    print("\n=== 顺序线路模块 ===")
    print("每页输入线路配置（例如 rabbkb），每两个字母代表一根线：")
    print("第一个字母：r(红), b(蓝), k(黑)；第二个字母：A, B, C。")

    # 定义规则表
    red_rules = {
        1: {'C'}, 2: {'B'}, 3: {'A'}, 4: {'A', 'C'}, 5: {'B'},
        6: {'A', 'C'}, 7: {'A', 'B', 'C'}, 8: {'A', 'B'}, 9: {'B'}
    }
    blue_rules = {
        1: {'B'}, 2: {'A', 'C'}, 3: {'B'}, 4: {'A'}, 5: {'B'},
        6: {'B', 'C'}, 7: {'C'}, 8: {'A', 'C'}, 9: {'A'}
    }
    black_rules = {
        1: {'A', 'B', 'C'}, 2: {'A', 'C'}, 3: {'B'}, 4: {'A', 'C'},
        5: {'B'}, 6: {'B', 'C'}, 7: {'A', 'B'}, 8: {'C'}, 9: {'C'}
    }

    # 累计颜色出现次数
    color_count = {'r': 0, 'b': 0, 'k': 0}
    result = []

    # 收集 4 页输入
    for page in range(1, 5):
        while True:
            config = input(f"第 {page} 页的线路配置（例如 rabbkb）：").strip().lower()
            if len(config) % 2 == 0 and all(c[0] in {'r', 'b', 'k'} and c[1] in {'a', 'b', 'c'} for c in zip(config[::2], config[1::2])):
                break
            print("无效输入！请输入偶数长度字符串，每两个字母为 r/b/k 和 a/b/c。")

        # 解析输入
        page_wires = {}
        for i in range(0, len(config), 2):
            color = config[i]
            letter = config[i + 1].upper()
            page_wires[i // 2 + 1] = {'color': color, 'letter': letter}
            color_count[color] += 1

        # 判断剪断
        cuts = []
        wire_list = list(page_wires.values())
        for idx, wire in enumerate(wire_list, 1):
            color = wire['color']
            letter = wire['letter']
            count = color_count[color]

            rules = {'r': red_rules, 'b': blue_rules, 'k': black_rules}[color]
            if count in rules and letter in rules[count]:
                cuts.append(color)

        if cuts:
            if len(wire_list) == 2 and cuts == [wire_list[1]['color']] and wire_list[1]['color'] == 'k':
                result.append(f"第 {page} 页：剪断第二根黑线")
            else:
                result.append(f"第 {page} 页：{''.join(cuts)}")
        else:
            result.append(f"第 {page} 页：无需剪线")

    return "\n".join(result) if result else "无剪线指令"