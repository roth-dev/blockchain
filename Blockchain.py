blockchain = [2, 2, 3]


def add_value(transition_amount: str):
    blockchain.append([blockchain[0], transition_amount])
    print(blockchain)


def get_user_input():
    """ Please enter amount you want append to blockchian LOL """
    return float(input("Please enter amount: "))


tax_amount = get_user_input()
add_value(tax_amount)
add_value(tax_amount)
