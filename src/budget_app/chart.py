# -*- coding: utf-8 -*-
"""Chart display module."""


def create_spend_chart_display(categories: list = None):
    """The chart shows the percentage spent in each category passed in to the function."""
    if categories is None:
        categories = []
    categories_list = []
    for category in categories:
        category_dict = {"name": category.name, "spent": category.get_spent()}
        categories_list.append(category_dict)
    total_budget = sum(category["spent"] for category in categories_list)
    for category in categories_list:
        category["percentage"] = get_percentage(category["spent"], total_budget)
    return bar_chart(categories_list)


def get_percentage(category_amount: float, categories_total: float):
    """Calculates the percentage of a category's amount relative
    to the total amount of all categories.

        Args:
            category_amount (float): The amount of the category.
            categories_total (float): The total amount of all categories.

        Returns:
            int: The percentage value rounded to the nearest multiple of 10.
    """
    return round(category_amount * 10 / categories_total * 10)


def bar_chart(categories_list: list):
    """
        Generates a bar chart representing the percentage spent by category.

        Args:
            categories_list (list): A list of dictionaries representing the
    categories and their percentages.

        Returns:
            str: The formatted bar chart as a string.

    """
    y_lines = []
    output_string = "Percentage spent by category\n"
    for i in range(100, -1, -10):
        line = [str(i)]
        for category in categories_list:
            if category["percentage"] >= i:
                line.append("o")
            else:
                line.append(" ")
        y_lines.append(line)

    for line in y_lines:
        percent = line[0]
        y_axis = f"{percent.rjust(3, ' ')}| "
        o_s = "  ".join(line[1:])
        output_string += f"{y_axis}{o_s}  \n"

    dashes = f"    -{'-' * len(categories_list) * 3}\n"
    output_string += dashes

    names = [category["name"] for category in categories_list]
    vertical_letters = sort_vertically(names)
    for line in vertical_letters:
        output_string += f"     {'  '.join(line)}  \n"

    return output_string.rstrip("\n")


def sort_vertically(strings):
    """
    Sorts the given list of strings vertically.

    Args:
        strings (List[str]): The list of strings to be sorted vertically.

    Returns:
        List[List[str]]: A list of lists representing the vertically sorted strings.

    Examples:
        >>> sort_vertically(["abc", "def", "ghi"])
        [['a', 'd', 'g'], ['b', 'e', 'h'], ['c', 'f', 'i']]
    """
    verticals = []
    max_length = max(len(s) for s in strings)
    for i in range(max_length):
        line = []
        for s in strings:
            if i < len(s):
                line.append(s[i])
            else:
                line.append(" ")
        verticals.append(line)
    return verticals
