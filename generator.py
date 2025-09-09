import random
import string


class DataCreatedUser:
    @staticmethod
    def generate_body():
        username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
        email = f"{username}@example.com"
        password = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(12))
        name = random.choice(['Иван', 'Петр', 'Мария', 'Анна', 'Сергей', 'Ольга', 'Алексей', 'Елена'])

        return {
            "email": email,
            "password": password,
            "name": name
        }