class Task:
    def __init__(self, title, status="pending"):
        self.title = title
        self.status = status  # "pending" or "done"

    def to_dict(self):
        return {
            "title": self.title,
            "status": self.status
        }
