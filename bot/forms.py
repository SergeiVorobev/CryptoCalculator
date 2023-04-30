from django import forms

from .models import OrdersData
from .algo_choices import ALGORITHM_CHOICES


class OrdersDataForm(forms.ModelForm):
    class Meta:
        model = OrdersData
        fields = ('coin', 'amount', 'n_orders', 'init_price', 'rate_changes', 'martingale',
                  'f_order_indent', 'algorithm', 'commission')

        labels = {
            'coin': 'Coin', 'amount': 'Total amount', 'n_orders': 'Number of orders',
            'init_price': 'Init price', 'rate_changes': 'Rate changes',
            'martingale': 'Martingale', 'f_order_indent': 'First order indent',
            'algorithm': 'Algorithm: short or long?',
            'commission': 'Commission rate'
        }
        widgets = {
            'coin': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '(like BTC)'}),
            'amount': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '(like 1000.00)'}),
            'n_orders': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '(like 10)'}),
            'init_price': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '(like 1000.00)'}),
            'rate_changes': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '%(like 5)'}),
            'martingale': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '%(like 5)'}),
            'f_order_indent': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '%(like 0.25)'}),
            'algorithm': forms.Select(choices=ALGORITHM_CHOICES, attrs={'class': 'form-control'}),
            'commission': forms.TextInput(attrs={'class': 'form-control',
                                                 'placeholder': '% (usually it is about 0.1 percent for deal amout)'}),
        }
