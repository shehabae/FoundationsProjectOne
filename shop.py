####################### DO NOT MODIFY THIS CODE ########################
menu = {
    "original cupcake": 2.000,
    "signature cupcake": 2.750,
    "coffee": 1.000,
    "tea": 0.900,
    "bottled water": 0.750
}
original_flavors = ["vanilla", "chocolate", "strawberry", "caramel", "raspberry"]
original_price = 2.000
signature_price = 2.750

############################# Start Here! ##############################
cupcake_shop_name = "mini bakes"
signature_flavors = ['vinegar', 'chilli', 'mashroom', 'chicken']
order_list = []


def print_menu():
    """
    Print the items in the menu dictionary.
    """
    # your code goes here!
    print('******** WELCOME TO MINI BAKES ********')
    print('Our menu:')
    for i in menu:
        print('- "%s" (KD %.3f)' % (i, menu[i]))

def print_originals():
    """
    Print the original flavor cupcakes.
    """
    print("Our original flavor cupcakes (KD %0.3f each):" % original_price)
    # your code goes here!
    for i in original_flavors:
        print('- "%s"' % i)

def print_signatures():
    """
    Print the signature flavor cupcakes.
    """
    print("Our signature flavor cupcake (KD %0.3f each):" % signature_price)
    # your code goes here!
    for i in signature_flavors:
        print('- "%s"' % i)



def is_valid_order(order):
    """
    Check if an order exists in the shop.
    """
    # your code goes here!
    if order in menu or order in original_flavors or order in signature_flavors:
        return True
    else:
        return False

def get_order():
    """
    Repeatedly ask customer for order until they end their order by typing "Exit".
    """
    order_list = []
    # your code goes here!
    print("What's your order? (Enter the exact spelling of the item you want, then press 'Enter'. Type 'Exit' to end your order)")
    not_done = True
    while not_done:
        order = input()
        if is_valid_order(order):
            order_list.append(order)
        elif order == 'Exit' or order == 'exit':
            not_done = False
        else:
            print('Please enter a valid order!')
    return order_list


def accept_credit_card(total):
    """
    Return whether an order is eligible for credit card payment.
    """
    # your code goes here!

    if total >= 5.000:
        return 'Your payment is eligible for credit card payment'
    else:
        return 'Your payment is not eligible for credit card payment'

def get_total_price(order_list):
    """
    Calculate and return total price of the order.
    """
    total = 0
    # your code goes here!

    for i in order_list:
        if i == 'original cupcake':
            total += 2.000
        elif i == 'signature cupcake':
            total += 2.750
        elif i == 'coffee':
            total += 1.000
        elif i == 'tea':
            total += 0.900
        elif i == 'bottled water':
            total += 0.750
        elif i == 'vanilla' or i == 'chocolate' or i == 'strawberry' or i == 'caramel' or i == 'raspberry':
            total += 2.000
        elif i == 'vinegar' or i == 'chilli' or i == 'mashroom' or i == 'chicken':
            total += 2.750
    return (total)


def print_order(order_list):
    """
    Print the order of the customer.
    """
    total = get_total_price(order_list)
    print()
    print('===============================')
    print("Your order is: ")
    print('===============================')
    # your code goes here!
    for i in order_list:
        print('- %s' % i)
    print()
    print('                =====')
    print('That will be KD %0.3f' % total)
    print('                =====')
    print(accept_credit_card(total))
    print()
    print('*** THANK YOU FOR VISITING MINI BAKES ***')
