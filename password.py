# 单词列表（包含 think 和 thing）
word_list = [
    "about", "after", "again", "below", "could", "every", "first", "found", "great",
    "house", "large", "learn", "never", "other", "place", "plant", "point", "right",
    "small", "sound", "spell", "still", "study", "their", "there", "these", "thing",
    "think", "three", "water", "where", "which", "world", "would", "write"
]


def find_possible_words():
    while True:
        # 提示用户输入一行 18 个字母
        prompt = "请输入第 1、2、5 个位置的字母："
        letters = input(prompt).strip().lower()

        # 验证输入
        if len(letters) != 18:
            print("错误：请输入 18 个字母（每个位置 6 个字母）！")
            continue

        # 将输入分成三组（每组 6 个字母）
        positions = [
            set(letters[0:6]),  # 第 1-6 个字母 -> 第 1 个位置
            set(letters[6:12]),  # 第 7-12 个字母 -> 第 2 个位置
            set(letters[12:18])  # 第 13-18 个字母 -> 第 5 个位置
        ]

        # 筛选符合条件的单词（只检查第 1、2、5 个字母）
        matching_words = []
        for word in word_list:
            # 检查单词的第 1、2、5 个字母是否在对应位置的集合中
            if (word[0] in positions[0] and  # 第 1 个字母
                    word[1] in positions[1] and  # 第 2 个字母
                    word[4] in positions[2]):  # 第 5 个字母
                matching_words.append(word)

        # 输出结果
        if len(matching_words) == 0:
            print("没有符合条件的单词！")
        else:
            print("符合条件的单词是:", ", ".join(matching_words))

        print("\n准备下一次输入（按 Ctrl+C 退出）...")


# 运行程序
try:
    find_possible_words()
except KeyboardInterrupt:
    print("\n程序已退出。")