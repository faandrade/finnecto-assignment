import json

from django.core.management.base import BaseCommand
from django.utils.dateparse import parse_datetime
from finnecto.models import Client, Order, OrderProduct, Product


class Command(BaseCommand):
    help = "Populate the database with data from JSON files"

    def handle(self, *args, **kwargs):
        with open("finnecto/data/purchase_requests.json") as f:
            purchase_requests = json.load(f)

        with open("finnecto/data/request_lines.json") as f:
            request_lines = json.load(f)

        clients = {}
        for pr in purchase_requests:
            client_name = pr["requester"]
            if client_name not in clients:
                client, created = Client.objects.get_or_create(name=client_name)
                clients[client_name] = client
            else:
                client = clients[client_name]

            order = Order.objects.create(
                requester=client,
                description=pr["description"],
                type=pr["type"],
                status=pr["status"],
                date=parse_datetime(pr["date"]),
            )

            for rl in request_lines:
                if rl["purchase_request_id"] == pr["id"]:
                    product, created = Product.objects.get_or_create(name=rl["product"])
                    OrderProduct.objects.create(
                        order=order,
                        product=product,
                        quantity=rl["quantity"],
                        price=rl["price"],
                        currency=rl["currency"],
                    )
