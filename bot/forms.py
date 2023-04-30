from django import forms
from django_bootstrap4.widgets import SwitchInput

from .models import OrdersData


class OrdersDataForm(forms.ModelForm):
    class Meta:
        model = OrdersData
        fields = ('coin', 'amount', 'n_orders', 'cur_price', 'rate_changes', 'martingale',
                  'f_order_indent', 'alg_long')

        labels = {
            'coin': 'Coin', 'amount': 'Total amount', 'n_orders': 'Number of orders',
            'init_price': 'Init price', 'rate_changes': 'Rate changes',
            'martingale': 'Martingale', 'f_order_indent': 'First order indent',
            'alg_long': 'Algorithm is long?',
        }
        widgets = {
            'coin': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '(like BTC)'}),
            'amount': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '(like 1000.00)'}),
            'n_orders': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '(like 10)'}),
            'init_price': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '(like 1000.00)'}),
            'rate_changes': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '%(like 5)'}),
            'martingale': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '%(like 5)'}),
            'f_order_indent': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '%(like 0.25)'}),
            'alg_long': SwitchInput(),
        }
