import random

from faker import Faker

from dto.user import User


class UserFactory:
    Faker.seed(seed=random.seed(777))
    factory = Faker()

    def create_user(self):
        return User(
            name=self.factory.name(),
            email=self.factory.email(),
            password=self.factory.password(),
            created_at=self.factory.date_time_ad(),
            updated_at=self.factory.date_time_ad(),
        )
