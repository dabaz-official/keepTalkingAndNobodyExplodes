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
        "1": ("线路", wires.solve),
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