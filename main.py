import wires
import button
import keypads
import simon_says
import whos_on_first
import memory
import morse_code
import complicated_wires
import wire_sequences
import maze
import password
from utils import get_serial_number, get_battery_count

def main():
    # 在程序开始时获取序列号和电池数量并缓存
    print("=== 初始化：请输入序列号和电池数量 ===")
    serial_info = get_serial_number()
    battery_count = get_battery_count()

    modules = {
        "1": ("线路", wires.solve),
        "2": ("按钮", button.solve),

        "4": ("四色方块", simon_says.solve),

        "8": ("复杂线路", complicated_wires.solve),
        "9": ("顺序线路", wire_sequences.solve),

        "11": ("密码", password.solve)
    }

    while True:
        print("\n=== Keep Talking and Nobody Explodes 拆弹助手 ===")
        print("请选择模块（输入 1-11）：")
        for num, (name, _) in modules.items():
            print(f"{num}. {name}")
        print("输入 'q' 退出")

        choice = input("\n你的选择：").strip().lower()

        if choice == 'q':
            print("感谢使用拆弹助手！")
            break

        if choice in modules:
            module_name, module_func = modules[choice]
            print(f"\n处理模块：{module_name}")
            result = module_func((serial_info, battery_count))
            print(f"结果：{result}")
        else:
            print("无效选择！请输入 1-11 或 'q'。")

if __name__ == "__main__":
    main()