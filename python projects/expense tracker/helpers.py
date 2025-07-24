def print_expenses(expenses):
    if not expenses:
        print("📭 Hech qanday xarajat kiritilmagan.")
        return

    print("\n📊 Xarajatlar ro‘yxati:")
    for idx, e in enumerate(expenses, start=1):
        print(f"{idx}. {e['date']} | {e['category']} | {e['title']} — 💰 {e['amount']} so‘m")

def total_amount(expenses):
    return sum(e['amount'] for e in expenses)

def filter_by_category(expenses, category):
    return [e for e in expenses if e['category'].lower() == category.lower()]
