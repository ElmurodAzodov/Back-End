def print_books(books):
    if not books:
        print("📭 Kitoblar yo‘q.")
    for idx, book in enumerate(books, start=1):
        print(f"{idx}. 📖 {book['title']} — ✍️ {book['author']} ({book['year']})")

def find_book(books, title):
    for book in books:
        if book['title'].lower() == title.lower():
            return book
    return None
