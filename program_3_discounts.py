def final_price(price, discount):
    return price - (price * discount)

def discount_print(name, overall):
    print(f"Final Price of {name} is {overall}")

discount_library = {
    "Costumer 1:": final_price(100, .10),
    "Costumer 2:": final_price(250, 0.05),
    "Costumer 3:": final_price(50, 0.05)
}

for name, overall in discount_library.items():
    discount_print(name, overall)
