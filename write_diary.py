from datetime import datetime

def write_diary(entry):
    # 获取当前日期和时间
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    # 将日记条目写入文件
    with open("diary.txt", "a", encoding="utf-8") as file:
        file.write(f"\n[{current_time}]\n{entry}\n")
    print("日记已成功保存！")

if __name__ == "__main__":
    print("欢迎使用日记记录小工具！")
    
    entry = input("请输入你今天的日记内容：\n")
    
    if entry.strip():
        write_diary(entry)
    else:
        print("日记内容不能为空，请重新输入。")
