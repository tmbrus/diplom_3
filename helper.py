import requests
from data import Ingredients


class CreatedOrder:
    @staticmethod
    def created_order(token):
        order_body = Ingredients.ingredients_body()
        header = {"Authorization": token}
        response = requests.post('https://stellarburgers.nomoreparties.site/api/orders',
                                 headers=header, json=order_body)
        return response.json()["order"]["number"]
