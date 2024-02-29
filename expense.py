class User:
    def _init_(self, username):
        self.username = username
        self.balance = 0
    def add_expense(self,amount):
        self.balance +=amount
    def settle_balance(self,amount):
        self.balance -=amount
class Expense:
    def _init_(self, description, amount, paid_by, users):
        self.description = description
        self.amount = amount
        self.paid_by = paid_by
        self.users = users
    def split_expense(self):
        num_users=len(self.users)
        per_person_amount=self.amount/num_users
        for user in self.users:
            if user != self.paid_by:
                user.add_expense(per_person_amount)
        self.paid_by.add_expense(-self.amount)
class ExpenseManager:
    def _init_(self):
        self.users = {}
    def add_user(self, username):
        self.users[username] = User(username)
    def add_expense(self, description, amount, paid_by, users):
        expense = Expense(description, amount, self.users[paid_by], [self.users[user] for user in users])
        expense.split_expense()
    def get_balance(self, user):
        return self.users[user].balance
if _name_ == "_main_":
    manager = ExpenseManager()
    manager.add_user("Kiru")
    manager.add_user("Miru")
    manager.add_user("Mithu")
    manager.add_expense("Dinner", 600, "Kiru", ["Miru", "Mithu"])
    manager.add_expense("Groceries", 250, "Miru", ["Kiru", "Mithu"])
    manager.add_expense("Shopping",300,"Mithu",["Kiru","Miru"])
    print("Kiru's balance:", manager.get_balance("Kiru"))
    print("Miru's balance:", manager.get_balance("Miru"))
    print("Mithu's balance:", manager.get_balance("Mithu"))
