from rest_framework import serializers
from Bank.transactions.transactions import Transaction

class TransactionsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'
       # fields = '__all__'