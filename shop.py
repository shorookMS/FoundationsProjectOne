####################### DO NOT MODIFY THIS CODE ########################
menu = {
    "original cupcake": 2,
    "signature cupcake": 2.750,
    "coffee": 1,
    "tea": 0.900,
    "bottled water": 0.750
}
original_flavors = ["vanilla", "chocolate", "strawberry", "caramel", "raspberry"]
original_price = 2
signature_price = 2.750

############################# Start Here! ##############################
cupcake_shop_name = "Sunrise Hill"
signature_flavors = ["taffy toffy","salty caramel","cereal break"]
order_list = []


def print_menu():
    """
    Print the items in the menu dictionary.
    """
    # your code goes here!
    print("\nOur menu:")
    for item, val in menu.items():
        print("- \"%s\" (KD %s)" % (item,val))


def print_originals():
    """
    Print the original flavor cupcakes.
    """
    print("\nOur original flavor cupcakes (KD %s each):" % original_price)
    # your code goes here!
    for flav in original_flavors:
        print("- \"%s\"" % flav)


def print_signatures():
    """
    Print the signature flavor cupcakes.
    """
    print("\nOur signature flavor cupcake (KD %s each):" % signature_price)
    
    # your code goes here!
    for flav in signature_flavors:
        print('- "%s"' % flav)


def is_valid_order(order):
    """
    Check if an order exists in the shop.
    """
    # your code goes here!
    if order.lower() in original_flavors :
        return True
    if order.lower() in menu.keys():
        return True
    elif order.lower() in signature_flavors :
        return True
    return False



def get_order():
    """
    Repeatedly ask customer for order until they end their order by typing "Exit".
    """
    order_list = []
    # your code goes here!
    print("\nWhat's your order? \n(Write the order with the same spelling please, and type 'Exit' to end your order.) ")
    while True:
        ordered = input()
        if ordered.lower() == 'exit':
            break
        elif is_valid_order(ordered):
            order_list.append(ordered)
        else :
            print("Your input was incorrect, please re:: enter your order.")

    return order_list


def accept_credit_card(total):
    """
    Return whether an order is eligible for credit card payment.
    """
    # your code goes here!
    if total < 5. :
        print("This order is not eligible for a credit card payment :<")
    else :
        print("This order is eligible for a credit card payment :D")



def get_total_price(order_list):
    """
    Calculate and return total price of the order.
    """
    total = 0
    # your code goes here!
    for ords in order_list:
        if ords in menu.keys():
            total += menu[ords]
        elif ords in original_flavors :
            total += original_price
        elif ords in signature_flavors :
            total += signature_price

    return total


def print_order(order_list):
    """
    Print the order of the customer.
    """
    
    print("\nYour order is: ")
    # your code goes here!
    for ords in order_list:
        print('- %s' % ords)
    total = get_total_price(order_list)
    print("\nThat will be %s" % total)
    accept_credit_card(total)
    print("Hope you enjoyed our service UwU. \nYou are always welcomed at %s!!!" % cupcake_shop_name)


