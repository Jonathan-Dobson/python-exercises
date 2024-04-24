# def print_circum(radius):
#     pi = 3.14159
#     circumference = 2 * pi * radius
#     print(f"The circumference of a circle with radius {radius} is {circumference}")

# print_circum(1)
# print_circum(2)
# print_circum(11)

# Include the following in your part 1 submission:

# The code for your print_circum function.
# The inputs and outputs to three calls of your print_circum.

print("\n")
# Part 2
# Welcome to your first project.  Develop a catalog for a company. Assume that this company sells three different Items. The seller can sell individual items or a combination of any two items. A gift pack is a special combination that contains all three items. Here are some special considerations:

# A. If a customer purchases individual items, he does not receive any discount.


# B. If a customer purchases a combo pack with two unique items, he gets a 10% discount.
combo_pack_discount = 0.10
# def combo_pack(item1, item2):
#     discount = 0.10
#     total_price = item1 + item2
#     discount_price = total_price - (total_price * discount)
#     return discount_price


# C. If the customer purchases a gift pack, he gets a 25% discount.
gift_pack_discount = 0.25
# def gift_pack(item1, item2, item3):
#     discount = 0.25
#     total_price = item1 + item2 + item3
#     discount_price = total_price - (total_price * discount)
#     return discount_price


# Write a function for the above scenario. Perform the calculations in code wherever applicable.  The function should be your own creation, not copied from any other source.  The final output should look like:
# def apply_discount(*items):
#     print(len(items), "items")

#     if len(items) == 1:
#         return items[0][0]
#     elif len(items) == 2:
#         return items[0] + items[1] - (items[0] + items[1] * combo_pack_discount)
#     elif len(items) == 3:
#         return (
#             items[0]
#             + items[1]
#             + items[2]
#             - (items[0] + items[1] + items[2] * gift_pack_discount)
#         )


# items = [("Item 1", 200), ("Item 2", 400), ("Item 3", 600)]


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
    {"name": "Item 1", "price": 200},
    {"name": "Item 2", "price": 400},
    {"name": "Item 3", "price": 600},
]
combo_pack_catalog = [
    {"name": "Combo 1(Item 1 + 2)", "price": apply_discount(1, 2)},
    {"name": "Combo 2(Item 1 + 3)", "price": apply_discount(1, 3)},
    {"name": "Combo 3(Item 2 + 3)", "price": apply_discount(2, 3)},
]
gift_pack_catalog = [
    {"name": "Gift Pack(Item 1 + 2 + 3)", "price": apply_discount(1, 2, 3)}
]
full_catalog = catalog + combo_pack_catalog + gift_pack_catalog
# print("Full Catalog", full_catalog)

# Define the table headers
headers = ("Product(S)", "Price")

# Calculate the maximum width of each column
# max_widths = [max(len(str(item)) for item in column) for column in zip(headers, *data)]
# max_widths = [max(len(str(item)) for item in column) for column in zip(*full_catalog)]
# max_widths = [
#     max(len(str(item["name"])) for item in column.values()) for column in full_catalog
# ]
# print("max widths", max_widths)
# max_widths = max([len(item["name"]) for item in full_catalog])
max_width_name = max([len(item["name"]) for item in full_catalog])
max_width_price = max([len(str(item["price"])) for item in full_catalog])

max_widths = [max_width_name, max_width_price]

print("max width name", max_width_name)
print("max width price", max_width_price)

print("Online Store")
print("----------------")

# Print the headers
print("  ".join(f"{header.ljust(width)}" for header, width in zip(headers, max_widths)))

# Print the separator line
print("  ".join("" * width for width in max_widths))


# Print each row of data
for row in full_catalog:
    # print(
    #     "  ".join(f"{str(item).ljust(width)}" for item, width in zip(row, max_widths))
    # )
    print(
        "  ".join(
            f"{str(item).ljust(width)}" for item, width in zip(row.values(), max_widths)
        )
    )

print("----------------")
print("For delivery Contact:8632584689")


# # Output of online store


# # Include the following in your part 2 submission:

# # The code for the function that you created.
# # The Output of the code.
# # A description of what feature(s) your function illustrates.
# # The code and its output must be explained technically. The explanation can be provided before or after the code, or in the form of comments within the code.
# # If you use an informational source, be sure to identify the source and share the link to the source you used.

# # Submission Instructions:
# # Submit the solutions to both part 1 and part 2 in one document.
# # Make sure your submission is double-spaced, using Times New Roman, 12-point font, with 1” margins.
# # The descriptive part of your response must be at least 200 words.
# # Use sources to support your arguments. Use high-quality, credible, relevant sources to develop ideas that are appropriate for the discipline and genre of the writing.
# # Use APA citations and references to support your work. Add a reference list at the end of the submission. For assistance with APA formatting, view the Learning Resource Center: Academic Writing.
# # Your submission should be clearly written, concise, well organized, and free of spelling and grammar errors. The grading will be based on an accurate solution to the problem and the quality of your writing.

# # This assignment will be assessed by your instructor. Please read the grading rubric on this page to understand how the instructor will assess your submission.
