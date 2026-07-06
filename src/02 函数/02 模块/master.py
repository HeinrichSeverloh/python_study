# master.py

def say_hello():
    print("👋 Hello! 我是 master.py 里的函数。")

print(f"DEBUG: 当前 master.py 的 __name__ 变量值是: {__name__}")

if __name__ == "__main__":
    print("✅ master.py 正在被直接运行！")
    say_hello()
else:
    print("⚠️ master.py 正在被导入（作为模块使用）。")