from django import forms
from .models import Transaction, Storage

class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['initial_volume', 'final_volume', 'temperature', 'date', 'oil_product', 'storage']  # Убедитесь, что 'storage' присутствует
