import requests
from data import ApiUrl


class UserMethods:

    @staticmethod
    def creating_user(body):
        return requests.post(f'{ApiUrl.BASE_URL}{ApiUrl.CREATING_USER_URL}', json=body)

    @staticmethod
    def delete_user(header):
        return requests.delete(f'{ApiUrl.BASE_URL}{ApiUrl.DELETE_USER_URL}', headers=header)


class OrderMethods:

    @staticmethod
    def creating_order(header, body):
        return requests.post(f'{ApiUrl.BASE_URL}{ApiUrl.CREATING_ORDER_URL}', headers=header, json=body)
