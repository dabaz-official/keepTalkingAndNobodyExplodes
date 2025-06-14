import wires
import button
import keypad
import simon_says
import whos_on_first
import memory
import morse_code
import complicated_wires
import wire_sequences
import maze
import password

def main():
    modules = {
        "1": ("简单电线", wires.solve),
        "2": ("按钮", button.solve),
        "3": ("符号键盘", keypad.solve),
        "4": ("Simon Says", simon_says.solve),
        "5": ("Who's on First", whos_on_first.solve),
        "6": ("记忆", memory.solve),
        "7": ("摩斯密码", morse_code.solve),
        "8": ("复杂电线", complicated_wires.solve),
        "9": ("电线序列", wire_sequences.solve),
        "10": ("迷宫", maze.solve),
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
            result = module_func()
            print(f"结果：{result}")
        else:
            print("无效选择！请输入 1-11 或 'q'。")

if __name__ == "__main__":
    main()