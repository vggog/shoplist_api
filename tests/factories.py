from faker import Faker

from src.app.user.models import UserModel


class UserFactory:
    user: UserModel = UserModel()
    faker: Faker = Faker('ru_RU')

    def get_user(
        self,
        username: str,
        name: str = faker.first_name(),
        surname: str = faker.last_name(),
        email: str = faker.ascii_free_email(),
        phone_number: str = faker.phone_number(),
    ) -> UserModel:
        
        self.user.username = username
        self.user.name = name
        self.user.surname = surname
        self.user.email = email
        self.user.phone_number = phone_number

        return self.user
