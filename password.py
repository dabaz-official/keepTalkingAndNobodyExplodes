# 单词列表
word_list = [
    "about", "after", "again", "below", "could", "every", "first", "found", "great",
    "house", "large", "learn", "never", "other", "place", "plant", "point", "right",
    "small", "sound", "spell", "still", "study", "their", "there", "these", "thing",
    "think", "three", "water", "where", "which", "world", "would", "write"
]


def find_unique_word():
    # 存储每个位置的字母集合
    positions = []

    # 提示用户输入 5 个位置的字母
    for i in range(5):
        prompt = f"请输入第 {i + 1} 个位置的 6 个字母（无需空格分隔，例如 abcdef）："
        letters = input(prompt).strip().lower()

        # 验证输入
        if len(letters) != 6:
            print(f"错误：第 {i + 1} 个位置需要输入 6 个字母！")
            return
        # 转换为集合以便快速查找
        positions.append(set(letters))

    # 筛选符合条件的单词
    matching_words = []
    for word in word_list:
        # 检查单词的每个字母是否在对应位置的集合中
        is_match = True
        for pos in range(5):
            if word[pos] not in positions[pos]:
                is_match = False
                break
        if is_match:
            matching_words.append(word)

    # 检查结果
    if len(matching_words) == 1:
        print("唯一符合条件的单词是:", matching_words[0])
    elif len(matching_words) == 0:
        print("没有符合条件的单词！")
    else:
        print("符合条件的单词不唯一:", ", ".join(matching_words))


# 运行程序
find_unique_word()