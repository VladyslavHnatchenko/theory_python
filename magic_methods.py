"""Enriching Your Python Classes With Dunder (Magic, Special) Methods."""

from functools import total_ordering


@total_ordering
class Account:
    """A simple account class."""
    def __init__(self, owner, amount=0):
        """
        This is constructor that lets us create objects from this class.
        """
        self.owner = owner
        self.amount = amount
        self._transaction = []

    def __repr__(self):
        return f"Account {self.owner}, {self.amount}"

    def __str__(self):
        return f"Account of {self.owner} with starting amount: {self.amount}"

    def add_transaction(self, amount):
        if not isinstance(amount, int):
            raise ValueError("please use int for amount")
        self._transaction.append(amount)

    @property
    def balance(self):
        return self.amount + sum(self._transaction)

    def __len__(self):
        return len(self._transaction)

    def __getitem__(self, position):
        return self._transaction[position]

    def __reversed__(self):
        return self[::-1]

    def __eq__(self, other):
        return self.balance == other.balance

    def __lt__(self, other):
        return self.balance < other.balance

    def __add__(self, other):
        owner = f"{self.owner}&{other.owner}"
        start_owner = self.amount + other.amount
        acc = Account(owner, start_owner)
        for t in list(self) + list(other):
            acc.add_transaction(t)
        return acc

    def __call__(self):
        print(f"Start amount: {self.amount}")
        print("Transaction: ")
        for transaction in self:
            print(transaction)
        print(f"\nBalance: {self.balance}")

    def __enter__(self):
        print("ENTER WITH: Making backup of transactions for rollback")
        self._copy_transaction = list(self._transaction)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("EXIT WITH:", end=" ")
        if exc_type:
            self._transactions = self._copy_transaction
            print("Rolling back to previous transactions.")
            print(f"Transaction resulted in {exc_type.__name__} ({exc_val})")
        else:
            print("Transaction OK")


def validate_transaction(acc, amount_to_add):
    with acc as a:
        print(f"Adding {amount_to_add} to account.")
        a.add_transaction(amount_to_add)
        print(f"New balance would be: {a.balance}")
        if a.balance < 0:
            raise ValueError('sorry cannot go in debt!')
