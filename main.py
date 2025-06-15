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
from utils import get_bomb_info

def main():
    modules = {
        "1": ("线路", wires.solve),
        "2": ("按钮", button.solve),
        "4": ("四色方块", simon_says.solve),
        "6": ("记忆", memory.solve),
        "8": ("复杂线路", complicated_wires.solve),
        "9": ("顺序线路", wire_sequences.solve),
        "10": ("密码", password.solve)
    }

    print("\n=== Keep Talking and Nobody Explodes 拆弹助手 ===")
    print("请先输入炸弹信息：")
    bomb_info = get_bomb_info()

    while True:
        print("\n请选择模块（输入 1-11）：")
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
            result = module_func(bomb_info)
            print(f"结果：{result}")
        else:
            print("无效选择！请输入 1-11 或 'q'。")

if __name__ == "__main__":
    main()