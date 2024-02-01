# -*- coding: utf-8 -*-
"""Chart display module."""


def create_spend_chart_display(categories: list = None):
    """The chart shows the percentage spent in each category passed in to the function."""
    if categories is None:
        categories = []
    categories_list = []
    for category in categories:
        category_dict = {"name": category.name, "total": category.get_balance()}
        categories_list.append(category_dict)
    total_budget = sum(category["total"] for category in categories_list)
    for category in categories_list:
        category["percentage"] = get_percentage(category["total"], total_budget)
    bar_chart(categories_list)


def get_percentage(category_amount: float, categories_total: float):
    """Calculates the percentage of a category's amount relative
    to the total amount of all categories.

        Args:
            category_amount (float): The amount of the category.
            categories_total (float): The total amount of all categories.

        Returns:
            int: The percentage value rounded to the nearest multiple of 10.
    """
    return round(category_amount * 10 / categories_total) * 10


def bar_chart(categories_list):
    """Chart a list of categories."""
    o_lines = []
    for i in range(100, -1, -10):
        line = [str(i)]
        for category in categories_list:
            if category["total"] <= i:
                line.append("o")
            else:
                line.append(" ")
            o_lines.append(line)

    for line in o_lines:
        y_axis = f"{line[0]}| "
        o_s = "  ".join(line[1:])
        print(f"{y_axis}{o_s}")
