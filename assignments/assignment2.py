print("Part 1")


def print_circum(radius):
    pi = 3.14159
    circumference = 2 * pi * radius
    print(f"The circumference of a circle with radius {radius} is {circumference}")


print_circum(1)
print_circum(2)
print_circum(11)

print("\n Part 2")


# Part 2
# Welcome to your first project.  Develop a catalog for a company. Assume that this company sells three different Items. The seller can sell individual items or a combination of any two items. A gift pack is a special combination that contains all three items. Here are some special considerations:
def print_catalog(price_format=None):
    # A. If a customer purchases individual items, he does not receive any discount.
    # B. If a customer purchases a combo pack with two unique items, he gets a 10% discount.
    combo_pack_discount = 0.10
    # C. If the customer purchases a gift pack, he gets a 25% discount.
    gift_pack_discount = 0.25

    def total_pack_price(pack):
        total = 0
        for item in pack:
            total += catalog[item - 1]["price"]
        return total

    def apply_discount(*pack):
        total = total_pack_price(pack)
        if len(pack) == 2:
            return total - (total * combo_pack_discount)
        elif len(pack) >= 3:
            return total - (total * gift_pack_discount)
        else:
            return total

    catalog = [
        {"name": "Item 1", "price": 200.0},
        {"name": "Item 2", "price": 400.0},
        {"name": "Item 3", "price": 600.0},
    ]
    combo_pack_catalog = [
        {"name": "Combo 1(Item 1 + 2)", "price": apply_discount(1, 2)},
        {"name": "Combo 2(Item 1 + 3)", "price": apply_discount(1, 3)},
        {"name": "Combo 3(Item 2 + 3)", "price": apply_discount(2, 3)},
    ]
    gift_pack_catalog = [
        {"name": "Combo 4(Item 1 + 2 + 3)", "price": apply_discount(1, 2, 3)}
    ]
    full_catalog = catalog + combo_pack_catalog + gift_pack_catalog

    def format_price(price):
        string = str(int(price * 100))
        return "$" + string[:-2] + "." + string[-2:]

    full_catalog_with_formatted_prices = [
        {"name": item["name"], "price": format_price(item["price"])}
        for item in full_catalog
    ]

    headers = ("Product(S)", "Price")

    max_width_name = max(
        [len(item["name"]) for item in full_catalog_with_formatted_prices]
    )
    max_width_price = max(
        [len(str(item["price"])) for item in full_catalog_with_formatted_prices]
    )
    max_widths = [max_width_name, max_width_price]

    print("Online Store")
    print("----------------")

    # Print the headers
    print(
        "  ".join(
            f"{header.ljust(width)}" for header, width in zip(headers, max_widths)
        )
    )

    selected_catalog = full_catalog
    if price_format == "USA":
        selected_catalog = full_catalog_with_formatted_prices

    # Print each row of data
    for row in selected_catalog:
        print(
            "  ".join(
                f"{str(item).ljust(width)}"
                for item, width in zip(row.values(), max_widths)
            )
        )
    # Print delivery contact
    print("----------------")
    print("For delivery Contact:9876468899\n")
    print("(Note: Prices formatted for USA)")


print_catalog()  # Matches the output in the assignment
print_catalog("USA")  # Added feature to show the formatted prices for my country
