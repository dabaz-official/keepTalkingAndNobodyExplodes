def solve(bomb_info):
    print("\n=== 四色方块 ===")

    # 询问并缓存失误次数
    while True:
        try:
            strikes = int(input("请告诉我有过几次失误（0, 1, 2）："))
            if strikes in [0, 1, 2]:
                break
            print("请输入 0、1 或 2！")
        except ValueError:
            print("请输入有效的数字（0, 1, 2）！")

    # 询问闪现的颜色序列
    color_sequence = input("请输入当前闪现的颜色序列（用 r, b, g, y 表示，1-5 个）：").strip().lower()

    # 验证输入
    valid_colors = {'r', 'b', 'g', 'y'}
    if not all(c in valid_colors for c in color_sequence) or len(color_sequence) not in range(1, 6):
        return "无效输入！请使用 r, b, g, y 表示 1-5 个颜色。"

    # 定义对应关系字典
    mapping = {}
    has_vowel = bomb_info["has_vowel"]
    if has_vowel:  # 情况 1：包含元音字母
        if strikes == 0:  # 情况 1.1
            mapping = {'r': 'b', 'b': 'r', 'g': 'y', 'y': 'g'}
        elif strikes == 1:  # 情况 1.2
            mapping = {'r': 'y', 'b': 'g', 'g': 'b', 'y': 'r'}
        elif strikes == 2:  # 情况 1.3
            mapping = {'r': 'g', 'b': 'r', 'g': 'y', 'y': 'b'}
    else:  # 情况 2：不包含元音字母
        if strikes == 0:  # 情况 2.1
            mapping = {'r': 'b', 'b': 'y', 'g': 'g', 'y': 'r'}
        elif strikes == 1:  # 情况 2.2
            mapping = {'r': 'r', 'b': 'b', 'g': 'y', 'y': 'g'}
        elif strikes == 2:  # 情况 2.3
            mapping = {'r': 'y', 'b': 'g', 'g': 'b', 'y': 'r'}

    # 生成按下序列
    press_sequence = ''.join(mapping.get(c, c) for c in color_sequence)

    return press_sequence