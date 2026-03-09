# Retail Store Billing System

products = {
    "rice": 50,
    "milk": 30,
    "bread": 40,
    "sugar": 45
}

cart = []
total = 0

while True:
    print("\n--- Retail Store Billing System ---")
    print("1. Add Product to Cart")
    print("2. Show Products")
    print("3. Generate Bill")
    print("4. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        item = input("Enter product name: ").lower()

        if item in products:
            qty = int(input("Enter quantity: "))
            price = products[item] * qty
            cart.append([item, qty, price])
            total = total + price
            print("Product added to cart.")
        else:
            print("Product not found.")

    elif choice == 2:
        print("\nAvailable Products:")
        for k, v in products.items():
            print(k,":",v)


    elif choice == 3:
        print("\n------ BILL ------")
        for c in cart:
            print("Item:", c[0], "Qty:", c[1], "Price:", c[2])

        print("Total Amount:", total)

        discount = 0
        if total > 1500:
            discount = total * 0.15
            print("Discount Applied:", discount)

        final = total - discount
        print("Final Amount:", final)

    elif choice == 4:
        print("Transaction Saved. Program Ended.")
        break

    else:
        print("Invalid Choice")