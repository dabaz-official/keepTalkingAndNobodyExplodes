def solve(params):
    _, _ = params  # 解包参数，暂不使用 serial_info 和 battery_count

    print("\n=== 密码模块 ===")
    print("每个位置有 6 个可能的字母（A-Z）。")
    print("请输入 3 组字母（每组 6 个字母，分别对应第 1、2、5 个位置）：")

    # 目标单词列表
    valid_words = [
        "about", "after", "again", "below", "could", "every", "first", "found",
        "great", "house", "large", "learn", "never", "other", "place", "plant",
        "point", "right", "small", "sound", "spell", "still", "study", "their",
        "there", "these", "thing", "think", "three", "water", "where", "which",
        "world", "would", "write"
    ]

    # 收集 3 组字母（每组 6 个）
    positions = []
    for i, pos in enumerate([1, 2, 5], 1):
        while True:
            letters = input(f"输入第 {pos} 个位置的 6 个字母（例如 ABCDEF）：").strip().upper()
            if len(letters) == 6 and all(c.isalpha() for c in letters):
                positions.append(set(letters))
                break
            print("错误：请输入 6 个字母（A-Z）！")

    # 筛选符合条件的单词（检查第 1、2、5 位）
    matching_words = []
    for word in valid_words:
        if (word[0] in positions[0] and  # 第 1 个字母
            word[1] in positions[1] and  # 第 2 个字母
            word[4] in positions[2]):    # 第 5 个字母
            matching_words.append(word)

    # 输出结果
    if len(matching_words) == 0:
        return "没有符合条件的单词"
    else:
        return "符合条件的单词是: " + ", ".join(matching_words)