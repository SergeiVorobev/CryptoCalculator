from django.shortcuts import render

# Create your views here.
def home(request, sn, n, order_q, start_price, first_marg, max_q_price, use_bnb=True):

    if use_bnb:
        commission = sn * 0.075 / 100 + 0.01  # I am adding 0.01$ just in case
    else:
        commission = sn * 0.1 / 100 + 0.01  # I am adding 0.01$ just in case

    # Calculate order amounts
    amounts = []
    order_amounts = 0
    for i in range(1, n):
        if i == 1:
            b1 = round(sn * (order_q - 1) / (order_q ** n - 1), 2)
            amounts.append(b1)
            order_amounts += b1
        if i in range(2, n):
            amount = round(b1 * order_q ** (i - 1), 2)
            amounts.append(amount)
            order_amounts += amount

    the_last_order = round(sn - commission - order_amounts, 2)
    amounts.append(the_last_order)
    order_amounts += the_last_order

    # Calculate order prices
    my_orders = {}
    o1_temp = start_price * (1 + first_marg / 100)
    bn = start_price + (start_price * max_q_price / 100)
    q_price = (bn / o1_temp) ** (1 / n)
    for i in range(1, n + 1):
        if i == 1:
            o1 = round(2 * start_price - o1_temp, 6)
            my_orders[o1] = amounts[i - 1]
        if i in range(2, n + 1):
            o = o1_temp * q_price ** (i - 1)
            o = round(2 * start_price - o, 6)
            my_orders[o] = amounts[i - 1]
    return render(request, 'calculator.html', {
                      # "name": name,
                      "my_orders": my_orders,
                     })