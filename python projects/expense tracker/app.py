from expense import Expense
from storage import load_expenses, save_expenses
from helpers import print_expenses, total_amount, filter_by_category

def main():
    expenses = load_expenses()

    while True:
        print("\n=== 💸 EXPENSE TRACKER ===")
        print("1. Barcha xarajatlar")
        print("2. Yangi xarajat qo‘shish")
        print("3. Kategoriya bo‘yicha filter")
        print("4. Umumiy summa")
        print("5. Chiqish")

        choice = input("Tanlang (1-5): ")

        if choice == "1":
            print_expenses(expenses)

        elif choice == "2":
            title = input("Nomi: ")
            amount = input("Miqdori (so‘m): ")
            category = input("Kategoriya (masalan: oziq-ovqat, transport): ")
            exp = Expense(title, amount, category)
            expenses.append(exp.to_dict())
            save_expenses(expenses)
            print("✅ Qo‘shildi.")

        elif choice == "3":
            cat = input("Kategoriya nomi: ")
            filtered = filter_by_category(expenses, cat)
            print_expenses(filtered)

        elif choice == "4":
            print(f"💰 Umumiy xarajat: {total_amount(expenses)} so‘m")

        elif choice == "5":
            print("👋 Chiqildi.")
            break

        else:
            print("⚠️ Noto‘g‘ri tanlov!")

if __name__ == "__main__":
    main()
