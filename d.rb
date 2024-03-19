class User:
    def __init__(self, n, a, e):
        self.name = n
        self.age = a
        self.email = e

    def get_name(self):
        return self.name

    def set_name(self, n):
        self.name = n

    def get_age(self):
        return self.age

    def set_age(self, a):
        self.age = a

    def get_email(self):
        return self.email

    def set_email(self, e):
        self.email = e
