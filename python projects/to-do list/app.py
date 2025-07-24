from task import Task
from storage import load_tasks, save_tasks
from helpers import print_tasks, get_index_choice

def main():
    tasks = load_tasks()

    while True:
        print("\n=== 📝 TO-DO LIST MANAGER ===")
        print("1. Vazifalar ro‘yxati")
        print("2. Yangi vazifa qo‘shish")
        print("3. Holatini o‘zgartirish (✅/🔄)")
        print("4. O‘chirish")
        print("5. Chiqish")

        choice = input("Tanlang (1-5): ")

        if choice == "1":
            print_tasks(tasks)

        elif choice == "2":
            title = input("Yangi vazifa nomi: ")
            new_task = Task(title)
            tasks.append(new_task.to_dict())
            save_tasks(tasks)
            print("✅ Qo‘shildi.")

        elif choice == "3":
            print_tasks(tasks)
            index = get_index_choice(tasks)
            if index is not None:
                task = tasks[index]
                task['status'] = "done" if task['status'] == "pending" else "pending"
                save_tasks(tasks)
                print("♻️ Holat yangilandi.")

        elif choice == "4":
            print_tasks(tasks)
            index = get_index_choice(tasks)
            if index is not None:
                removed = tasks.pop(index)
                save_tasks(tasks)
                print(f"🗑 O‘chirildi: {removed['title']}")

        elif choice == "5":
            print("👋 Chiqildi.")
            break

        else:
            print("⚠️ Noto‘g‘ri tanlov!")

if __name__ == "__main__":
    main()
