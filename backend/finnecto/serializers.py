from rest_framework import serializers

from .models import Client, Order, OrderProduct, Product


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


class OrderProductSerializer(serializers.ModelSerializer):
    product = ProductSerializer()

    class Meta:
        model = OrderProduct
        fields = "__all__"


class OrderSerializer(serializers.ModelSerializer):
    requester = ClientSerializer()
    products = OrderProductSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = "__all__"
