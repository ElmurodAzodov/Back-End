def print_tasks(tasks):
    if not tasks:
        print("📭 Hozircha vazifalar yo‘q.")
        return

    print("\n📋 Vazifalar ro‘yxati:")
    for idx, task in enumerate(tasks, start=1):
        status_icon = "✅" if task['status'] == "done" else "🔄"
        print(f"{idx}. {status_icon} {task['title']}")

def get_index_choice(tasks):
    try:
        choice = int(input("Raqamini tanlang: "))
        if 1 <= choice <= len(tasks):
            return choice - 1
        else:
            print("⚠️ Xato raqam.")
    except ValueError:
        print("⚠️ Raqam kiriting.")
    return None
