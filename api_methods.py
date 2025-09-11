import requests
from curl import ApiUrl


class UserMethods:

    @staticmethod
    def creating_user(body):
        return requests.post(
            ApiUrl.CREATING_USER_URL,
            json=body)

    @staticmethod
    def delete_user(header):
        return requests.delete(
            ApiUrl.DELETE_USER_URL,
            headers=header)


class OrderMethods:

    @staticmethod
    def creating_order(header, body):
        return requests.post(
            ApiUrl.CREATING_ORDER_URL,
            headers=header,
            json=body)
