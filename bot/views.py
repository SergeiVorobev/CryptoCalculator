from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponseRedirect

from .forms import OrdersDataForm
from .models import OrdersData


# Create your views here.
def home(request):
    submitted = False

    if request.method == "POST":
        form = OrdersDataForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            return HttpResponseRedirect('?submitted=True')
    else:
        form = OrdersDataForm
        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'base.html', {'form': form, 'submitted': submitted, })


def calc(request):
    
    qs = OrdersData.objects.order_by('-id').first()
    alg = qs.algorithm
    sn = qs.amount
    n = qs.n_orders
    orders_coef = qs.martingale
    start_price = qs.init_price
    first_marg = qs.f_order_indent
    max_q_price = qs.rate_changes
    comm = qs.commission
    # sn, n, orders_coef, start_price, first_marg, max_q_price, use_bnb=True, is_long=True

    commission = sn * comm / 100 + 0.01  # I am adding 0.01$ just in case

    # Calculate order amounts
    amounts = []
    order_amounts = 0
    for i in range(1, n):
        if i == 1:
            b1 = round(sn * (orders_coef/100) / ((1 + orders_coef/100) ** n - 1), 2)
            amounts.append(b1)
            order_amounts += b1
        if i in range(2, n):
            amount = round(b1 * (1 + orders_coef / 100) ** (i - 1), 2)
            amounts.append(amount)
            order_amounts += amount

    the_last_order = round(sn - commission - order_amounts, 2)
    amounts.append(the_last_order)
    order_amounts += the_last_order
    print(order_amounts)

    # Calculate order prices
    my_orders = {}
    f_order_price_temp = start_price * (1 + first_marg / 100)
    l_order_price_temp = start_price + (start_price * max_q_price / 100)
    orders_coef = (l_order_price_temp / f_order_price_temp) ** (1 / n)
    
    if alg == "long":    
        for i in range(1, n + 1):
            if i == 1:
                o1_price = round(2 * start_price - f_order_price_temp, 4) # 2 * 29,000 - 29,750 =  28,250
                my_orders[o1_price] = amounts[i - 1] # {28,250: 795.05}
            if i in range(2, n + 1):
                o = f_order_price_temp * orders_coef ** (i - 1)
                o = round(2 * start_price - o, 4)
                my_orders[o] = amounts[i - 1]
    else:
        for i in range(1, n + 1):
            if i == 1:
                o1_price = round(f_order_price_temp, 4)
                my_orders[o1_price] = amounts[i - 1] # {28,250: 795.05}
            if i in range(2, n + 1):
                o = round(f_order_price_temp * orders_coef ** (i - 1), 4)
                my_orders[o] = amounts[i - 1]
        
    return render(request, 'calculator.html', {
                    "data": qs,
                    "orders": my_orders,
                    })


from django.shortcuts import get_object_or_404

def edit_data(request, id):
    # Get the specific data by ID or show 404 if not found
    instance = get_object_or_404(OrdersData, id=id)

    if request.method == "POST":
        form = OrdersDataForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('calc')  # Redirect to the calculation results
    else:
        # Pre-fill the form with existing data
        form = OrdersDataForm(instance=instance)

    return render(request, 'base.html', {'form': form, 'data': instance})


def delete_data(request, id):
    instance = get_object_or_404(OrdersData, id=id)
    if request.method == "POST":
        instance.delete()
        return redirect('home')  # Redirect to the home page after deletion

    return render(request, 'delete_confirm.html', {'data': instance})
