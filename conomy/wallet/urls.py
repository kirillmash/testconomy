from django.urls import path
from .views import WalletAPIView, TransactionListAPIView, TransactionListByWalletAPIView


urlpatterns = [
    path('wallets/', WalletAPIView.as_view()),
    path('add_wallet/', WalletAPIView.as_view()),
    path('delete_wallet/<int:pk>/', WalletAPIView.as_view()),
    path('update_wallet/<int:pk>/', WalletAPIView.as_view()),
    path('transactions/', TransactionListAPIView.as_view()),
    path('add_transaction/', TransactionListAPIView.as_view()),
    path('delete_transaction/<int:pk>/', TransactionListAPIView.as_view()),
    path('transactions/<int:pk>/', TransactionListByWalletAPIView.as_view()),

]
