import random

import requests


def make_order(DeliveryFeeRequestPayload_):
    url = "https://daas-public-api.development.dev.woltapi.com/merchants/6364e0108018ce361efafcc3/delivery-order"
    h = {"Authorization": "Bearer 8OJSTMKSAGoWUkO3ETXtQwZEiKYymzH4mAmbG1icJVU"}
    x = requests.post(url, json=DeliveryFeeRequestPayload_, headers=h)
    # data = x.json()
    # url = data['tracking']['url']
    print(x.text)


def DelFeeReq_strg(start, end):
    strg = {
        "pickup": {"location": {"formatted_address": start}},
        "dropoff": {"location": {"formatted_address": end}},
    }
    return strg


class User:
    def __init__(self, name, address, phone_number, email):
        self.name = name
        self.address = address
        self.phone_number = phone_number
        self.email = email


class Order:
    def __init__(self, seller, buyer, merchant_order_reference_id):
        self.seller = seller
        self.buyer = buyer
        self.merchant_order_reference_id = merchant_order_reference_id


def makeOrderStrg(order):
    strg = {
        "pickup": {
            "location": {"formatted_address": order.seller.address},
            "comment": "The box is in front of the door",
            "contact_details": {
                "name": order.seller.name,
                "phone_number": order.seller.phone_number,
                "send_tracking_link_sms": 0,
            },
        },
        "dropoff": {
            "location": {"formatted_address": order.buyer.address},
            "contact_details": {
                "name": order.buyer.name,
                "phone_number": order.buyer.phone_number,
                "send_tracking_link_sms": 0,
            },
            "comment": "Leave at the door, please",
        },
        "customer_support": {
            "email": "info@wolt.com",
            "phone_number": "003708599126",
            "url": "https://wolt.com/en/contact",
        },
        "merchant_order_reference_id": order.merchant_order_reference_id,
        "is_no_contact": 0,
        "contents": [
            {
                "count": 1,
                "description": "plastic bag",
                "identifier": random.randint(10**6, 10**7),
                "tags": [],
            }
        ],
        "tips": [],
        "min_preparation_time_minutes": 0,
    }

    return strg


def main():

    buyer = User("gino", "Arkadiankatu 3-6", "+358123456789", "gino.bello@gmail.com")
    seller = User(
        "ugo", "Otakaari 24, 02150 Espoo", "+358123456789", "ugo.bello@gmail.com"
    )
    order = Order(seller, buyer, 2537)
    order_strg = makeOrderStrg(order)
    make_order(order_strg)


main()
