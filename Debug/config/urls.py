from django.urls import path

from .views import (UserCheckBalanceView)

urlpatterns = [
    # path('', UserListView.as_view(), name='user_list'),
    # path('create/', UserCreateView.as_view(), name='user_create'),
    # path('<int:pk>/', UserUpdateView.as_view(), name='user_update'),
    path(
        'check-balance/', UserCheckBalanceView.as_view(),
        name='user_check_balance'
    )
]