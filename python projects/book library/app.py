from book import Book
from storage import load_books, save_books
from helpers import print_books, find_book

def main():
    books = load_books()
    while True:
        print("\n=== 📚 BOOK LIBRARY ===")
        print("1. Kitoblar ro‘yxati")
        print("2. Qo‘shish")
        print("3. Qidirish")
        print("4. O‘chirish")
        print("5. Chiqish")

        choice = input("Tanlang (1-5): ")

        if choice == "1":
            print_books(books)

        elif choice == "2":
            title = input("Kitob nomi: ")
            author = input("Muallif: ")
            year = input("Yili: ")
            new_book = Book(title, author, year)
            books.append(new_book.to_dict())
            save_books(books)
            print("✅ Qo‘shildi!")

        elif choice == "3":
            title = input("Qidirilayotgan nom: ")
            found = find_book(books, title)
            if found:
                print(f"📖 {found['title']} — ✍️ {found['author']} ({found['year']})")
            else:
                print("🚫 Topilmadi.")

        elif choice == "4":
            title = input("O‘chirish uchun nom: ")
            book = find_book(books, title)
            if book:
                books.remove(book)
                save_books(books)
                print("🗑 O‘chirildi.")
            else:
                print("❌ Bunday kitob yo‘q.")

        elif choice == "5":
            print("👋 Chiqildi.")
            break
        else:
            print("⚠️ Noto‘g‘ri tanlov!")

if __name__ == "__main__":
    main()
