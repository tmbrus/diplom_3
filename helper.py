import requests
from data import Ingredients
from curl import ApiUrl

class CreatedOrder:
    @staticmethod
    def created_order(token):
        order_body = Ingredients.ingredients_body()
        header = {"Authorization": token}
        response = requests.post(
            ApiUrl.CREATING_ORDER_URL,
            headers=header,
            json=order_body)
        return response.json()["order"]["number"]
