from rest_framework import serializers
from Bank.transactions.transactions import Transactiona

class TransactionsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Transactiona
        fields = '__all__'
       # fields = '__all__'