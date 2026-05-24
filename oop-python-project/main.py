# =========================
# Library System
# =========================

class LibraryBook:
    library_name = "Central Library"
    total_books = 0

    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

        LibraryBook.total_books += 1

    def summary(self):
        return (
            f"{self.title} by {self.author} -- "
            f"{self.pages} pages | Library: {LibraryBook.library_name}"
        )

    @classmethod
    def get_total(cls):
        return f"Books in the system: {cls.total_books}"


# =========================
# Shopping Cart System
# =========================

class ShoppingCart:
    def __init__(self):
        self.items = []
        self.discount = 0

    def add_item(self, name, price):
        self.items.append((name, price))

    def apply_discount(self, percent):
        self.discount = percent

    def total(self):
        subtotal = sum(price for name, price in self.items)
        final_total = subtotal - (subtotal * self.discount / 100)
        return round(final_total, 2)


# =========================
# Bank Account System
# =========================

class BankAccount:
    bank_name = "National Bank"

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient funds"
        else:
            self.balance -= amount
            return self.balance


# =========================
# Student System
# =========================

class Student:
    student_count = 0

    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa

        Student.student_count += 1

    def is_honor(self):
        return self.gpa >= 3.5

    @classmethod
    def total(cls):
        return f"Total students: {cls.student_count}"


# =========================
# Example Usage
# =========================
if __name__ == "__main__":

    book1 = LibraryBook("1984", "George Orwell", 328)
    book2 = LibraryBook("Animal Farm", "George Orwell", 112)

    cart = ShoppingCart()
    cart.add_item("Laptop", 1000)
    cart.add_item("Mouse", 50)
    cart.apply_discount(10)

    account = BankAccount("Nihad", 500)
    account.deposit(200)
    account.withdraw(100)

    student1 = Student("Ali", 3.8)

    print(book1.summary())
    print(LibraryBook.get_total())
    print(cart.total())
    print(account.balance)
    print(student1.is_honor())
    print(Student.total())
