from drf_spectacular.utils import OpenApiParameter, extend_schema, extend_schema_view
from finnecto.models import Order
from finnecto.serializers import OrderSerializer
from rest_framework.viewsets import ReadOnlyModelViewSet


@extend_schema_view(
    list=extend_schema(
        description="Retrieve a list of orders filtered by client_id",
        parameters=[
            OpenApiParameter(
                name="client_id",
                type=str,
                description="Filter orders by client_id",
            ),
        ],
    )
)
class OrderViewSet(ReadOnlyModelViewSet):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()  # needed by router, overwritten by get_queryset

    def get_queryset(self):
        client_id = self.request.query_params.get("client_id")
        if client_id:
            return Order.objects.filter(requester=client_id)
        return Order.objects.all()
