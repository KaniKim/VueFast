from faker import Faker

from dto.user import User


class UserFactory:
    factory = Faker()

    def create_user(self):
        return User(name=self.factory.user_name(), email=self.factory.email)
