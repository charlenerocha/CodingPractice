class Bank:

    def __init__(self, balance: List[int]):
        self.balance = balance

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        account1 -= 1
        account2 -= 1
        if account1 >= 0 and account1 < len(self.balance) and self.balance[account1] >= money and money >= 0 and account2 >= 0 and account2 < len(self.balance):
            self.balance[account1] -= money
            self.balance[account2] += money
            return True
        return False

    def deposit(self, account: int, money: int) -> bool:
        account -= 1
        if account >= 0 and account < len(self.balance) and money >= 0:
            self.balance[account] += money
            return True
        return False

    def withdraw(self, account: int, money: int) -> bool:
        account -= 1
        if account >= 0 and account < len(self.balance) and self.balance[account] >= money and money >= 0:
            self.balance[account] -= money
            return True
        return False


# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)