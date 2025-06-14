def solve(params):
    _, battery_count = params  # 解包参数，仅使用 battery_count

    print("\n=== 按钮模块 ===")

    # 第一步：电池数量 >= 2
    if battery_count >= 2:
        has_detonate = input("按钮上是否写着“引爆”？（y/n）：").strip().lower()
        if has_detonate == 'y':
            return "按下按钮并立即松开"

    # 第二步：电池数量 >= 3
    if battery_count >= 3:
        has_frk = input("是否有写着 FRK 的指示灯亮？（y/n）：").strip().lower()
        if has_frk == 'y':
            return "按下按钮并立即松开"

    # 第三步：红色按钮写有“按住”
    is_red_hold = input("是否是写有“按住”的红色按钮？（y/n）：").strip().lower()
    if is_red_hold == 'y':
        return "按下按钮并立即松开"
    else:
        return "蓝色光条：4\n黄色光条：5\n其他颜色光条：1"