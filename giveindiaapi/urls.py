
from django.urls import path,include

from .views import Transfer,AccountList


urlpatterns = [
    path('transfer', Transfer.as_view()),
    path('list', AccountList.as_view()),
]