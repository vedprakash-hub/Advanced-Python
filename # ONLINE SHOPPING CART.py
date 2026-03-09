# ONLINE SHOPPING CART

items = ['smartphone','book','laptop','watch','fridge','oven']
price = [20000,500,50000,4000,15000,25000]

cart = []
cart_total = []

while True:
  print(" WELCOME TO ONLINE SHOPPING CART!! \n")

  print("1. Add Item")
  print("2. Remove Item")
  print("3. View Cart")
  print("4. Checkout")
  print("5. Exit")

  ch = input("Enter your choice (between 1-5): ")

  if ch == '1':
    print("\nThe list of available items are: \n")
    for i in range(len(items)):
      print(i+1,items[i]," - Rs",price[i])

    obj = int(input("Enter the item number you want to add to your cart: "))

    cart.append(items[obj-1])
    cart_total.append(price[obj-1])
    print("\n Item Added To Your Cart! \n")

  elif ch == '2':
    print("\n Your Cart Contains: \n")
    for i in range(len(cart)):
      print(i+1,cart[i]," - Rs",cart_total[i])

    name = input("Enter the name of the item you want to remove: ")
    if name in cart:
      num = cart.index(name)
      cart.remove(name)
      cart_total.pop(num)
      print("\n Item Removed From Your Cart!\n\n")
    else:
      print("\n Item not found in your cart!\n\n")

  elif ch == '3':
    print("\n Your Cart Contains: \n")
    if not cart:
      print("Your cart is empty.\n")
    else:
      for i in range(len(cart)):
        print(i+1,cart[i]," - Rs",cart_total[i])

  elif ch == '4':
    print("\n The Total Amount for your purchases are: ",sum(cart_total))

    if sum(cart_total) > 25000:
      print("For Final Price being Above 25000 30% discount availed.\n The Final Price is: ",sum(cart_total)*0.7)
      print("Please proceed to Exit.\n\n")
    else:
      print("Final Price is: ",sum(cart_total))
      print("Please proceed to Exit.\n\n")

  elif ch == '5':
    print("Thank You For Using Our Online Shopping Cart!")
    break