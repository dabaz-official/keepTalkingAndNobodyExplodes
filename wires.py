from utils import get_serial_number

def solve():
    print("\n=== 简单电线模块 ===")
    while True:
        try:
            num_wires = int(input("请输入电线数量（3-6）："))
            if num_wires not in [3, 4, 5, 6]:
                print("电线数量必须在3到6之间！")
                continue
            break
        except ValueError:
            print("请输入有效的数字！")

    if num_wires == 3:
        # 3 根电线的判断逻辑
        has_red = input("是否有红线？（y/n）：").strip().lower()
        if has_red != 'y':
            return 2  # 剪第二根电线

        is_last_white = input("最后一根线是否是白线？（y/n）：").strip().lower()
        if is_last_white == 'y':
            return 3  # 剪第三根电线

        while True:
            try:
                blue_count = int(input("有几根蓝线？（请输入数字）："))
                if blue_count < 0 or blue_count > 3:
                    print("蓝线数量必须在0到3之间！")
                    continue
                break
            except ValueError:
                print("请输入有效的数字！")

        if blue_count in [2, 3]:
            return "剪最后一根蓝线"
        else:
            return 3  # 剪第三根电线（蓝线为 0 或 1）

    elif num_wires == 4:
        # 4 根电线的判断逻辑
        while True:
            try:
                red_count = int(input("有几根红线？（请输入数字）："))
                if red_count < 0 or red_count > 4:
                    print("红线数量必须在0到4之间！")
                    continue
                break
            except ValueError:
                print("请输入有效的数字！")

        if red_count in [2, 3]:
            _, _, is_last_digit_odd = get_serial_number()
            if is_last_digit_odd:
                return "剪最后一根红线"
            # 若偶数，继续到问题3

        if red_count == 0:
            is_last_yellow = input("最后一根线是否是黄线？（y/n）：").strip().lower()
            if is_last_yellow == 'y':
                return 1  # 剪第一根电线
            # 若不是黄线，继续到问题3

        # 问题3：蓝线数量
        while True:
            try:
                blue_count = int(input("有几根蓝线？（请输入数字）："))
                if blue_count < 0 or blue_count > 4:
                    print("蓝线数量必须在0到4之间！")
                    continue
                break
            except ValueError:
                print("请输入有效的数字！")

        if blue_count == 1:
            return 1  # 剪第一根电线

        # 问题4：黄线数量
        while True:
            try:
                yellow_count = int(input("有几根黄线？（请输入数字）："))
                if yellow_count < 0 or yellow_count > 4:
                    print("黄线数量必须在0到4之间！")
                    continue
                break
            except ValueError:
                print("请输入有效的数字！")

        if yellow_count in [2, 3, 4]:
            return 4  # 剪第四根电线
        else:
            return 2  # 剪第二根电线

    elif num_wires == 5:
        # 5 根电线的判断逻辑
        is_last_black = input("最后一根线是否是黑线？（y/n）：").strip().lower()
        if is_last_black == 'y':
            _, _, is_last_digit_odd = get_serial_number()
            if is_last_digit_odd:
                return 4  # 剪第四根电线
            # 若偶数，继续到问题2

        # 问题2：红线数量
        while True:
            try:
                red_count = int(input("有几根红线？（请输入数字）："))
                if red_count < 0 or red_count > 5:
                    print("红线数量必须在0到5之间！")
                    continue
                break
            except ValueError:
                print("请输入有效的数字！")

        if red_count == 1:
            # 问题3：黄线数量
            while True:
                try:
                    yellow_count = int(input("有几根黄线？（请输入数字）："))
                    if yellow_count < 0 or yellow_count > 5:
                        print("黄线数量必须在0到5之间！")
                        continue
                    break
                except ValueError:
                    print("请输入有效的数字！")

            if yellow_count in [2, 3, 4, 5]:
                return 1  # 剪第一根电线
            # 若黄线为 0 或 1，继续到问题4

        # 问题4：是否有黑线（特殊情况：若问题1回答 'y'，直接返回 1）
        if is_last_black == 'y':
            return 1  # 剪第一根电线

        has_black = input("是否有黑线？（y/n）：").strip().lower()
        if has_black == 'y':
            return 1  # 剪第一根电线
        else:
            return 2  # 剪第二根电线

    elif num_wires == 6:
        # 6 根电线的判断逻辑
        while True:
            try:
                yellow_count = int(input("有几根黄线？（请输入数字）："))
                if yellow_count < 0 or yellow_count > 6:
                    print("黄线数量必须在0到6之间！")
                    continue
                break
            except ValueError:
                print("请输入有效的数字！")

        if yellow_count == 0:
            _, _, is_last_digit_odd = get_serial_number()
            if is_last_digit_odd:
                return 3  # 剪第三根电线
            # 若偶数，继续到问题3

        if yellow_count == 1:
            # 问题2：白线数量
            while True:
                try:
                    white_count = int(input("有几根白线？（请输入数字）："))
                    if white_count < 0 or white_count > 6:
                        print("白线数量必须在0到6之间！")
                        continue
                    break
                except ValueError:
                    print("请输入有效的数字！")

            if white_count in [0, 1]:
                pass  # 继续到问题3
            else:
                return 4  # 剪第四根电线

        # 问题3：是否有红线
        has_red = input("是否有红线？（y/n）：").strip().lower()
        if has_red == 'y':
            return 4  # 剪第四根电线
        else:
            return 6  # 剪第六根电线