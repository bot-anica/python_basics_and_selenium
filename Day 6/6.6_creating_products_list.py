# ---------- CREATING PRODUCTS LIST
print("----- CREATING PRODUCTS LIST -----")

products_number = int(input("How many groceries can you take away from the store? "))

products_list = []


def add_product(product_index):
    product = input(f"Enter {product_index + 1} product: ")

    if product in products_list:
        print(f"{product} is already in the list")
        add_product(product_index)
    else:
        products_list.append(product)


for i in range(products_number):
    add_product(i)

print(products_list)
