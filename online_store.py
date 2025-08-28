store = {
    "laptop": {"price": 1200, "quantity": 5},
    "headphones": {"price": 150, "quantity": 10},
    "mouse": {"price": 40, "quantity": 20},
}
def start():
    while True:
        print("----online store menu-----")
        print("1. add product")
        print("2. update stock")
        print("3. sell product")
        print("4. display inventory")
        print("5. total potential sales")
        print("6. exit")
        choice = input("enter your choice (1-7)")
        if choice == "1":
            add_product(store)
        elif choice == "2":
            update_stock(store)
        elif choice == "3":
            sell_product(store)
        elif choice == "4":
            display_inventory(store)
        elif choice == "5":
            total_potential_sales(store)
        elif choice == "6":
            print("goodbye kryssie")
            break
        else:
            print("invalid choice")
def add_product(store):
    name =input("enter product name:") 
    price = float(input("enter product price:"))
    quantity = int(input("enter product qty:"))
    if name in store:
        print(f"{name} already exists.")
    else:
        store[name] = {"price": price, "quantity": quantity}
        print(f"{name} added")
def update_stock(store):
    name = input("enter product to update:")
    quantity = input("enter product quantity to update:")
    if name not in store:
        print(f"{name} does not exist")
    else:
        store[name]["quantity"] = quantity
    print(f"stock for {name} updated to {quantity}")
def sell_product(store):
    name = input("enter prodct name to sell:")
    quantity = int(input("enter quantity to sell:"))
    if name not in store:
        print(f"{name} not found")
    elif store[name]["quantity"] < quantity:
        print(f"not enough stock for {name}")
    else:
        store[name]["quantity"] -= quantity
        print(f"sold {quantity} of {name}. remaining:{store[name]['quantity']}")
def display_inventory(store):
    print("INVENTORY")
    if not store:
        print("no product in store")
        return 0
    count = 0
    for product, details in store.items():
        print(f"{product} - price:{details['price']}, quantity:{details['quantity']}")
        count += 1
    print(f"\ntotal number of products:{count}")
    return count
def total_potential_sales(store):
    print("TOTAL POTENTIAL SALES")
    if not store:
        print("no products in store")
        return 0
    total = 0
    for product, details in store.items():
        total += details['price'] * details['quantity']
    print(f"total value of all remaining stock: {total}")
    return total
start()
