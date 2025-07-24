from contact import Contact
from storage import load_contacts, save_contacts
from helpers import find_contact, print_contacts

def main():
    contacts = load_contacts()
    while True:
        print("\n=== CONTACT MANAGER ===")
        print("1. Kontaktlar ro‘yxati")
        print("2. Qo‘shish")
        print("3. Qidirish")
        print("4. O‘chirish")
        print("5. Chiqish")

        choice = input("Tanlang (1-5): ")

        if choice == "1":
            print_contacts(contacts)

        elif choice == "2":
            name = input("Ism: ")
            phone = input("Telefon: ")
            email = input("Email: ")
            years_old = input("Yosh: ")
            new_contact = Contact(name, phone, email, years_old)
            contacts.append(new_contact.to_dict())
            save_contacts(contacts)
            print("✅ Qo‘shildi!")

        elif choice == "3":
            name = input("Qidirilayotgan ism: ")
            found = find_contact(contacts, name)
            if found:
                print(f"👤 {found['name']} | 📞 {found['phone']} | ✉️ {found['email']}")
            else:
                print("🚫 Topilmadi.")

        elif choice == "4":
            name = input("O‘chirish uchun ism: ")
            contact = find_contact(contacts, name)
            if contact:
                contacts.remove(contact)
                save_contacts(contacts)
                print("🗑 O‘chirildi.")
            else:
                print("❌ Bunday kontakt yo‘q.")

        elif choice == "5":
            print("👋 Chiqildi.")
            break
        else:
            print("⚠️ Noto‘g‘ri tanlov!")

if __name__ == "__main__":
    main()
