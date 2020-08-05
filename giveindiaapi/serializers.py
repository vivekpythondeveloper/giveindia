from rest_framework import serializers

from .models import Account,TransferAmount


class AccountSerializer(serializers.ModelSerializer):

    class Meta:
        model                       = Account
        fields                      = ['account_id','amount','type_of']

class TransferSerializer(serializers.ModelSerializer):

    class Meta:
        model                       = TransferAmount
        fields                      = ['transfer_from_account','transfer_to_account','transfer_amount']