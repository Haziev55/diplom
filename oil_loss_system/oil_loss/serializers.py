from rest_framework import serializers
from .models import OilProduct, Storage, Transaction

class OilProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = OilProduct
        fields = '__all__'

class StorageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Storage
        fields = '__all__'

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'


from rest_framework import serializers
from .models import Transaction, Storage

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ['initial_volume', 'final_volume', 'temperature', 'date', 'oil_product', 'storage']  # Добавьте 'storage'


from rest_framework import serializers
from .models import Transaction

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ['id', 'initial_volume', 'final_volume', 'temperature', 'date', 'oil_product', 'storage']
