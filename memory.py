def solve(bomb_info):
    print("\n=== 记忆 ===")
    print("每个阶段请输入屏幕显示的数字（1-4），然后输入按下按钮的位置和数字（例如 12 表示位置 1、数字 2）。")

    # 存储每阶段的按下信息
    stage_data = {}
    results = []

    # 循环 5 个阶段
    for stage in range(1, 6):
        print(f"\n阶段 {stage}：")

        # 获取显示数字
        while True:
            try:
                display_num = int(input("请输入屏幕显示的数字（1-4）："))
                if display_num in [1, 2, 3, 4]:
                    break
                print("请输入 1 到 4 的数字！")
            except ValueError:
                print("请输入有效的数字！")

        # 根据阶段和显示数字生成按下指令
        instruction = None
        if stage == 1:
            if display_num in [1, 2]:
                instruction = "第二个位置"
            elif display_num == 3:
                instruction = "第三个位置"
            elif display_num == 4:
                instruction = "第四个位置"
        elif stage == 2:
            if display_num == 1:
                instruction = "数字为4"
            elif display_num in [2, 4]:
                instruction = f"第 {stage_data[1]['position']} 个位置"
            elif display_num == 3:
                instruction = "第一个位置"
        elif stage == 3:
            if display_num == 1:
                instruction = f"数字为 {stage_data[2]['number']}"
            elif display_num == 2:
                instruction = f"数字为 {stage_data[1]['number']}"
            elif display_num == 3:
                instruction = "第三个位置"
            elif display_num == 4:
                instruction = "数字为4"
        elif stage == 4:
            if display_num == 1:
                instruction = f"第 {stage_data[1]['position']} 个位置"
            elif display_num == 2:
                instruction = "第一个位置"
            elif display_num in [3, 4]:
                instruction = f"第 {stage_data[2]['position']} 个位置"
        elif stage == 5:
            if display_num == 1:
                instruction = f"数字为 {stage_data[1]['number']}"
            elif display_num == 2:
                instruction = f"数字为 {stage_data[2]['number']}"
            elif display_num == 3:
                instruction = f"数字为 {stage_data[4]['number']}"
            elif display_num == 4:
                instruction = f"数字为 {stage_data[3]['number']}"

        # 保存并输出指令
        results.append(f"阶段 {stage}: {instruction}")
        print(f"请按下：{instruction}")

        # 获取用户输入的按下信息
        while True:
            try:
                press_info = input("请输入按下按钮的位置和数字（例如 12）：").strip()
                if len(press_info) == 2 and press_info.isdigit():
                    position = int(press_info[0])
                    number = int(press_info[1])
                    if position in [1, 2, 3, 4] and number in [1, 2, 3, 4]:
                        stage_data[stage] = {"position": position, "number": number}
                        break
                print("请输入两位数字（例如 12），位置和数字均为 1-4！")
            except ValueError:
                print("请输入有效的两位数字！")

    # 返回所有阶段的结果
    return "\n".join(results)