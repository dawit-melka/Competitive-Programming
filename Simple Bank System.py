class Bank:

    def __init__(self, balance: List[int]):
        self.balance = balance
        

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        valid_acc1 = 0 < account1 <= len(self.balance)
        valid_acc2 = 0 < account2 <= len(self.balance)

        if not valid_acc1 or not valid_acc2:
            return False
        
        if money > self.balance[account1-1]:
            return False
        
        self.balance[account1-1] -= money
        self.balance[account2-1] += money
        return True

    def deposit(self, account: int, money: int) -> bool:
        valid_acc = 0 < account <= len(self.balance)
        if not valid_acc:
            return False
        
        self.balance[account-1] += money
        return True

    def withdraw(self, account: int, money: int) -> bool:
        valid_acc = 0 < account <= len(self.balance)

        if not valid_acc or money > self.balance[account-1]:
            return False
        
        self.balance[account-1] -= money
        return True
