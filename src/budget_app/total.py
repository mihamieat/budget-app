# -*- coding: utf-8 -*-
"""Module related to the output display."""


def display_category_total(category_name: str, ledger: list, total: int):
    """Generates a formatted text representation of a category's ledger.

    Args:
        category_name (str): The name of the category.
        ledger (list): The ledger containing the category's operations.

    Returns:
        str: The formatted text representation of the category's ledger.
    """
    text = f"{padding_text(category_name)}\n"
    for operation in ledger:
        amount = f"{operation['amount']:.2f}"
        description = f"{operation['description'][:23]}"
        text += f"{description:<23}{amount:>7}\n"
    text += f"Total: {total}"

    return text


def padding_text(text: str, width: int = 30):
    """Pads the given text with asterisks to achieve the specified width.

    Args:
        text (str): The text to pad.
        width (int, optional): The desired width of the padded text. Defaults to 30.

    Returns:
        str: The padded text.
    """
    padding_length = width - len(text)

    if padding_length <= 0:
        return text[:width]

    left_padding = padding_length // 2
    right_padding = padding_length - left_padding
    return f"{'*' * left_padding}{text}{'*' * right_padding}"
