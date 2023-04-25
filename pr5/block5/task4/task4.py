import sqlite3
from hypothesis import given
import hypothesis.strategies as st


class BankAccount:
    def __init__(self, account_number):
        self.account_number = account_number
        self.conn = sqlite3.connect('bank.db')
        self.cursor = self.conn.cursor()
        self.cursor.execute(
            "CREATE TABLE IF NOT EXISTS accounts (account_number INTEGER PRIMARY KEY, balance REAL)")
        self.conn.commit()

    def deposit(self, amount):
        self.cursor.execute(
            "UPDATE accounts SET balance = balance + ? WHERE account_number = ?", (amount, self.account_number))
        self.conn.commit()
        return f"{amount} средств успешно зачислены на счет {self.account_number}"

    def withdraw(self, amount):
        self.cursor.execute(
            "SELECT balance FROM accounts WHERE account_number = ?", (self.account_number,))
        balance = self.cursor.fetchone()[0]
        self.cursor.execute(
            "UPDATE accounts SET balance = balance - ? WHERE account_number = ?", (amount, self.account_number))
        self.conn.commit()
        return f"{amount} средств успешно сняты с счета {self.account_number}"

    def check_balance(self):
        self.cursor.execute(
            "SELECT balance FROM accounts WHERE account_number = ?", (self.account_number,))
        balance = self.cursor.fetchone()[0]
        return f"Баланс счета {self.account_number}: {balance}"

    def close_account(self):
        self.cursor.execute(
            "DELETE FROM accounts WHERE account_number = ?", (self.account_number,))
        self.conn.commit()
        return f"Счет {self.account_number} закрыт"

    def create_account(self, balance):
        self.cursor.execute(
            "INSERT INTO accounts (account_number, balance) VALUES (?, ?)", (self.account_number, balance))
        self.conn.commit()
        return f"Счет {self.account_number} успешно создан"

class TestBankAccount:
    @given(st.floats(allow_nan=False, allow_infinity=False))
    def test_deposit(self, amount):
        account_number = 1234567890
        account = BankAccount(account_number)
        initial_balance = self.get_balance(account_number)
        account.deposit(amount)
        new_balance = self.get_balance(account_number)
        assert new_balance == initial_balance + amount

    @given(st.floats(allow_nan=False, allow_infinity=False))
    def test_withdraw(self, amount):
        account_number = 1234567890
        account = BankAccount(account_number)
        account.deposit(amount)
        initial_balance = self.get_balance(account_number)
        account.withdraw(amount)
        new_balance = self.get_balance(account_number)
        assert new_balance == initial_balance - amount

    @given(st.floats(allow_nan=False, allow_infinity=False))
    def test_create_account(self, balance):
        account_number = 1234567890
        account = BankAccount(account_number)
        account.create_account(balance)
        assert self.account_exists(account_number)

    @given(st.floats(allow_nan=False, allow_infinity=False))
    def test_close_account(self, balance):
        account_number = 1234567890
        account = BankAccount(account_number)
        account.create_account(balance)
        account.close_account()
        assert not self.account_exists(account_number)

    def get_balance(self, account_number):
        conn = sqlite3.connect('bank.db')
        cursor = conn.cursor()
        cursor.execute(
            "SELECT balance FROM accounts WHERE account_number = ?", (account_number,))
        balance = cursor.fetchone()[0]
        conn.close()
        return balance

    def account_exists(self, account_number):
        conn = sqlite3.connect('bank.db')
        cursor = conn.cursor()
        cursor.execute(
            "SELECT COUNT(*) FROM accounts WHERE account_number = ?", (account_number,))
        count = cursor.fetchone()[0]
        conn.close()
        return count == 1


bank = BankAccount(12312312312)
print(bank.create_account(200))

# test_bank = TestBankAccount()
# test_bank.test_create_account()