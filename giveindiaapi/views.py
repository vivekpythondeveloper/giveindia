from django.shortcuts import render

from rest_framework import generics

from django.http import JsonResponse

from datetime import datetime



from .models import Account,TransferAmount
from .serializers import AccountSerializer,TransferSerializer


class AccountList(generics.ListAPIView):
    serializer_class               = AccountSerializer
    queryset                       = Account.objects.all()


class Transfer(generics.ListAPIView):
    serializer_class               = TransferSerializer
    queryset                       = TransferAmount.objects.all()

    def post(self, request, *args, **kwargs):
        transfer_from              = self.request.POST['transfer_from_account']
        transfer_to                = self.request.POST['transfer_to_account']
        transfer_amount            = self.request.POST['transfer_amount']
        response                   = {}
        if transfer_from == transfer_to:
            response['errorCode']      = '1'
            response['errorMessage']   = 'from account can not be same as to account!'
            return JsonResponse(response)
        if len(transfer_amount) == 0:
            response['errorCode']      = '1'
            response['errorMessage']   = 'amount must be greater than zero!'
            return JsonResponse(response)
        if int(transfer_amount) > 5000000:
            response['errorCode']      = '1'
            response['errorMessage']   = 'amount must be 500000 paise aur less than!'
            return JsonResponse(response)
        try:
            print("transfer acount",transfer_from)
            account_from                        = Account.objects.get(account_id=1)
            account_to                          = Account.objects.get(account_id=2)
        except Exception as e:
            print("error is",str(e))
            response['errorCode']      = '1'
            response['errorMessage']   = 'no account found!'
            return JsonResponse(response)
        if int(transfer_amount) > account_from.amount:
            response['errorCode']      = '1'
            response['errorMessage']   = 'amount is greater than the blance have!'
            return JsonResponse(response)
        transferAmount                 = TransferAmount(transfer_from_account=account_from,transfer_to_account=account_to,
                                        transfer_amount=int(transfer_amount),transfered_at= datetime.now())
        transferAmount.save()
        account_from.amount = account_from.amount - int(transfer_amount)
        account_from.save()

        account_to.amount = account_to.amount + int(transfer_amount)
        account_to.save()

        transferTotals = TransferAmount.objects.all()
        totalTransfer = 0
        for transferTotal in transferTotals:
            if transferTotal.transfer_from_account.account_id == account_from.account_id:
                totalTransfer = totalTransfer + transferTotal.transfer_amount
        
        response['newSrcBalance']        = account_from.amount
        response['totalDestBalance']     = totalTransfer
        response['transferedAt']         = transferAmount.transfered_at
        
        return JsonResponse(response)

