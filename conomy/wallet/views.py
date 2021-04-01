from django.http import Http404
from rest_framework import status
from rest_framework.exceptions import ParseError
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Wallet, Transaction
from .serializers import WalletSerializer, TransactionSerializer


class WalletAPIView(APIView):

    @staticmethod
    def get_object(pk):
        try:
            return Wallet.objects.get(pk=pk)
        except Wallet.DoesNotExist:
            raise Http404

    def get(self, request):
        wallet = Wallet.objects.all()
        serializer = WalletSerializer(wallet, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = WalletSerializer(data=request.data)
        if not serializer.is_valid():
            raise ParseError(detail=serializer.errors)
        wallet = Wallet.objects.create(**serializer.validated_data)
        serialized = WalletSerializer(wallet)
        return Response(serialized.data, status=status.HTTP_201_CREATED)

    def put(self, request, pk):
        wallet = self.get_object(pk)
        serializer = WalletSerializer(wallet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        wallet = self.get_object(pk)
        wallet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class TransactionListAPIView(APIView):

    @staticmethod
    def get_object(pk):
        try:
            return Transaction.objects.get(pk=pk)
        except Transaction.DoesNotExist:
            raise Http404

    def get(self, request):
        transactions = Transaction.objects.all().select_related('wallet')
        serializer = TransactionSerializer(transactions, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = TransactionSerializer(data=request.data)
        if not serializer.is_valid():
            raise ParseError(detail=serializer.errors)
        transaction = Transaction.objects.create(**serializer.validated_data)
        serialized = TransactionSerializer(transaction)
        return Response(serialized.data, status=status.HTTP_201_CREATED)

    def delete(self, request, pk):
        transaction = self.get_object(pk)
        transaction.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class TransactionListByWalletAPIView(APIView):

    def get(self, request, pk):
        wallet = WalletAPIView.get_object(pk)
        transactions = Transaction.objects.filter(wallet=wallet)
        serializer = TransactionSerializer(transactions, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)







