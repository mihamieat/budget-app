# -*- coding: utf-8 -*-
"""Module contains category object."""
from budget_app.total import display_category_total
from budget_app.chart import create_spend_chart_display


class Category:
    """Category class.
    Budged categories are food, clothing and entertainment.
    """

    def __init__(self, name: str):
        """Initializes a new Category object with the given name.

        Args:
            name (str): The name of the category.
        """
        self.name = name
        self.ledger = []

    def __str__(self):
        """Returns a string representation of the Category object.

        Returns:
            str: The string representation of the Category object.
        """
        total = self.get_balance()
        return display_category_total(self.name, self.ledger, total)

    def deposit(self, amount: float, description: str = ""):
        """Append money and add new deposit object to ledger."""
        deposit = {"amount": amount, "description": description}

        self.ledger.append(deposit)

    def withdraw(self, amount: float, description: str = ""):
        """Withdraw money and add operation to ledger.
        Returns fals if money is not enough.
        """
        available = self.check_funds(amount)
        if available:
            withdraw = {"amount": -amount, "description": description}
            self.ledger.append(withdraw)
        return available

    def get_balance(self):
        """Returns the current balance."""
        return sum(operation["amount"] for operation in self.ledger)

    def transfer(self, amount: float, category_obj):
        """Transfers a specified amount from the current category to the specified category.

        Args:
            amount (float): The amount to transfer.
            category_obj: The category object to transfer the amount to.

        Returns:
            bool: True if the transfer is successful, False otherwise.
        """
        tr_description = f"Transfer to {category_obj.name}"
        dest_description = f"Transfer from {self.name}"
        if self.check_funds(amount):
            self.withdraw(amount, tr_description)
            category_obj.deposit(amount, dest_description)
            return True
        return False

    def check_funds(self, amount: float):
        """Checks if the current category has enough funds to cover the specified amount.

        Args:
            amount (float): The amount to check.

        Returns:
            bool: True if the current category has enough funds, False otherwise.
        """

        fund = self.get_balance()
        return amount <= fund


def create_spend_chart(categories: list):
    """Display chart"""
    create_spend_chart_display(categories)
