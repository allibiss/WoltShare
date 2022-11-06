import requests


def get_fee(DeliveryFeeRequestPayload_):
    url = "https://daas-public-api.development.dev.woltapi.com/merchants/6364e0108018ce361efafcc3/delivery-fee"
    h = {"Authorization": "Bearer 8OJSTMKSAGoWUkO3ETXtQwZEiKYymzH4mAmbG1icJVU"}
    x = requests.post(url, json=DeliveryFeeRequestPayload_, headers=h)
    data = x.json()
    fee = data["fee"]["amount"]
    return fee


def DelFeeReq_strg(start, end):
    strg = {
        "pickup": {"location": {"formatted_address": start}},
        "dropoff": {"location": {"formatted_address": end}},
    }
    return strg


def main():
    start = "Arkadiankatu 3-6"
    end = "Otakaari 24, 02150 Espoo"
    myStrgReq = DelFeeReq_strg(start, end)
    get_fee(myStrgReq)
