from django.contrib import admin

# Register your models here.

from .models import AccountType, Account

class AccountAdmin(admin.ModelAdmin):
    fields                  = ('amount', 'type_of')
    list_display            = ['account_id','amount']

class AccountTypeAdmin(admin.ModelAdmin):
    fields                  = ('account_type',)
    list_display            = ['account_type']

admin.site.register(Account, AccountAdmin)
admin.site.register(AccountType, AccountTypeAdmin)
