class Contact:
    def __init__(self, name, phone, email, years_old):
        self.name = name,
        self.phone = phone,
        self.email = email
        
    def to_dict(self):
        return {
            "name": self.name,
            "phone": self.phone,
            "email": self.email
        }
