def find_contact(contacts, name):
    for contact in contacts:
        if contact['name'].lower() == name.lower():
            return contact
    return None

def print_contacts(contacts):
    if not contacts:
        print("📭 Kontaktlar yo‘q.")
    for c in contacts:
        print(f"👤 {c['name']} | 📞 {c['phone']} | ✉️ {c['email']}")
